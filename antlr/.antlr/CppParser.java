// Generated from d:/Users/EC/Desktop/PMF/3rd year/Kompilatori/KK Projekat/antlr/CppParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CppParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CLASS=1, PUBLIC=2, PRIVATE=3, VOID=4, INT=5, FLOAT=6, DOUBLE=7, CHAR=8, 
		BOOL=9, STRING=10, STD=11, RETURN=12, NEW=13, IF=14, ELSE=15, WHILE=16, 
		INCLUDE=17, LBRACE=18, RBRACE=19, LPAREN=20, RPAREN=21, SEMI=22, COMMA=23, 
		DOT=24, ASSIGN=25, PLUS=26, MINUS=27, STAR=28, DIV=29, QUOTE=30, COLON=31, 
		COLONCOLON=32, LEFT_SHIFT=33, RIGHT_SHIFT=34, LT=35, GT=36, ID=37, NUMBER=38, 
		STRING_LITERAL=39, LINE_COMMENT=40, BLOCK_COMMENT=41, WS=42;
	public static final int
		RULE_program = 0, RULE_preprocessorDirective = 1, RULE_classDeclaration = 2, 
		RULE_classBody = 3, RULE_classBodyElement = 4, RULE_accessModifier = 5, 
		RULE_methodDefinition = 6, RULE_functionDefinition = 7, RULE_parameterList = 8, 
		RULE_type = 9, RULE_variableDeclaration = 10, RULE_statement = 11, RULE_methodCall = 12, 
		RULE_argumentList = 13, RULE_functionCall = 14, RULE_expression = 15, 
		RULE_shiftExpression = 16, RULE_additiveExpression = 17, RULE_multiplicativeExpression = 18, 
		RULE_postfixExpression = 19, RULE_postfixOp = 20, RULE_primaryExpression = 21, 
		RULE_assignement = 22, RULE_objectDeclaration = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "preprocessorDirective", "classDeclaration", "classBody", 
			"classBodyElement", "accessModifier", "methodDefinition", "functionDefinition", 
			"parameterList", "type", "variableDeclaration", "statement", "methodCall", 
			"argumentList", "functionCall", "expression", "shiftExpression", "additiveExpression", 
			"multiplicativeExpression", "postfixExpression", "postfixOp", "primaryExpression", 
			"assignement", "objectDeclaration"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'public'", "'private'", "'void'", "'int'", "'float'", 
			"'double'", "'char'", "'bool'", "'string'", "'std'", "'return'", "'new'", 
			"'if'", "'else'", "'while'", "'#include'", "'{'", "'}'", "'('", "')'", 
			"';'", "','", "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'\"'", "':'", 
			"'::'", "'<<'", "'>>'", "'<'", "'>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CLASS", "PUBLIC", "PRIVATE", "VOID", "INT", "FLOAT", "DOUBLE", 
			"CHAR", "BOOL", "STRING", "STD", "RETURN", "NEW", "IF", "ELSE", "WHILE", 
			"INCLUDE", "LBRACE", "RBRACE", "LPAREN", "RPAREN", "SEMI", "COMMA", "DOT", 
			"ASSIGN", "PLUS", "MINUS", "STAR", "DIV", "QUOTE", "COLON", "COLONCOLON", 
			"LEFT_SHIFT", "RIGHT_SHIFT", "LT", "GT", "ID", "NUMBER", "STRING_LITERAL", 
			"LINE_COMMENT", "BLOCK_COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CppParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CppParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CppParser.EOF, 0); }
		public List<PreprocessorDirectiveContext> preprocessorDirective() {
			return getRuleContexts(PreprocessorDirectiveContext.class);
		}
		public PreprocessorDirectiveContext preprocessorDirective(int i) {
			return getRuleContext(PreprocessorDirectiveContext.class,i);
		}
		public List<ClassDeclarationContext> classDeclaration() {
			return getRuleContexts(ClassDeclarationContext.class);
		}
		public ClassDeclarationContext classDeclaration(int i) {
			return getRuleContext(ClassDeclarationContext.class,i);
		}
		public List<FunctionDefinitionContext> functionDefinition() {
			return getRuleContexts(FunctionDefinitionContext.class);
		}
		public FunctionDefinitionContext functionDefinition(int i) {
			return getRuleContext(FunctionDefinitionContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137439092722L) != 0)) {
				{
				setState(52);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(48);
					preprocessorDirective();
					}
					break;
				case 2:
					{
					setState(49);
					classDeclaration();
					}
					break;
				case 3:
					{
					setState(50);
					functionDefinition();
					}
					break;
				case 4:
					{
					setState(51);
					statement();
					}
					break;
				}
				}
				setState(56);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(57);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PreprocessorDirectiveContext extends ParserRuleContext {
		public TerminalNode INCLUDE() { return getToken(CppParser.INCLUDE, 0); }
		public TerminalNode LT() { return getToken(CppParser.LT, 0); }
		public TerminalNode ID() { return getToken(CppParser.ID, 0); }
		public TerminalNode GT() { return getToken(CppParser.GT, 0); }
		public PreprocessorDirectiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preprocessorDirective; }
	}

	public final PreprocessorDirectiveContext preprocessorDirective() throws RecognitionException {
		PreprocessorDirectiveContext _localctx = new PreprocessorDirectiveContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_preprocessorDirective);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(INCLUDE);
			setState(60);
			match(LT);
			setState(61);
			match(ID);
			setState(62);
			match(GT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassDeclarationContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(CppParser.CLASS, 0); }
		public TerminalNode ID() { return getToken(CppParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(CppParser.LBRACE, 0); }
		public ClassBodyContext classBody() {
			return getRuleContext(ClassBodyContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(CppParser.RBRACE, 0); }
		public TerminalNode SEMI() { return getToken(CppParser.SEMI, 0); }
		public ClassDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDeclaration; }
	}

	public final ClassDeclarationContext classDeclaration() throws RecognitionException {
		ClassDeclarationContext _localctx = new ClassDeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_classDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(CLASS);
			setState(65);
			match(ID);
			setState(66);
			match(LBRACE);
			setState(67);
			classBody();
			setState(68);
			match(RBRACE);
			setState(69);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassBodyContext extends ParserRuleContext {
		public List<ClassBodyElementContext> classBodyElement() {
			return getRuleContexts(ClassBodyElementContext.class);
		}
		public ClassBodyElementContext classBodyElement(int i) {
			return getRuleContext(ClassBodyElementContext.class,i);
		}
		public ClassBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classBody; }
	}

	public final ClassBodyContext classBody() throws RecognitionException {
		ClassBodyContext _localctx = new ClassBodyContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_classBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137438957564L) != 0)) {
				{
				{
				setState(71);
				classBodyElement();
				}
				}
				setState(76);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClassBodyElementContext extends ParserRuleContext {
		public AccessModifierContext accessModifier() {
			return getRuleContext(AccessModifierContext.class,0);
		}
		public MethodDefinitionContext methodDefinition() {
			return getRuleContext(MethodDefinitionContext.class,0);
		}
		public VariableDeclarationContext variableDeclaration() {
			return getRuleContext(VariableDeclarationContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(CppParser.SEMI, 0); }
		public ClassBodyElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classBodyElement; }
	}

	public final ClassBodyElementContext classBodyElement() throws RecognitionException {
		ClassBodyElementContext _localctx = new ClassBodyElementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_classBodyElement);
		try {
			setState(82);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				accessModifier();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				methodDefinition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(79);
				variableDeclaration();
				setState(80);
				match(SEMI);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AccessModifierContext extends ParserRuleContext {
		public TerminalNode PUBLIC() { return getToken(CppParser.PUBLIC, 0); }
		public TerminalNode COLON() { return getToken(CppParser.COLON, 0); }
		public TerminalNode PRIVATE() { return getToken(CppParser.PRIVATE, 0); }
		public AccessModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_accessModifier; }
	}

	public final AccessModifierContext accessModifier() throws RecognitionException {
		AccessModifierContext _localctx = new AccessModifierContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_accessModifier);
		try {
			setState(88);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PUBLIC:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				match(PUBLIC);
				setState(85);
				match(COLON);
				}
				break;
			case PRIVATE:
				enterOuterAlt(_localctx, 2);
				{
				setState(86);
				match(PRIVATE);
				setState(87);
				match(COLON);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodDefinitionContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(CppParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(CppParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CppParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(CppParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CppParser.RBRACE, 0); }
		public TerminalNode PUBLIC() { return getToken(CppParser.PUBLIC, 0); }
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public MethodDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDefinition; }
	}

	public final MethodDefinitionContext methodDefinition() throws RecognitionException {
		MethodDefinitionContext _localctx = new MethodDefinitionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_methodDefinition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PUBLIC) {
				{
				setState(90);
				match(PUBLIC);
				}
			}

			setState(93);
			type();
			setState(94);
			match(ID);
			setState(95);
			match(LPAREN);
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137438957552L) != 0)) {
				{
				setState(96);
				parameterList();
				}
			}

			setState(99);
			match(RPAREN);
			setState(100);
			match(LBRACE);
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137438961648L) != 0)) {
				{
				{
				setState(101);
				statement();
				}
				}
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(107);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDefinitionContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(CppParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(CppParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CppParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(CppParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(CppParser.RBRACE, 0); }
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public FunctionDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDefinition; }
	}

	public final FunctionDefinitionContext functionDefinition() throws RecognitionException {
		FunctionDefinitionContext _localctx = new FunctionDefinitionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_functionDefinition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			type();
			setState(110);
			match(ID);
			setState(111);
			match(LPAREN);
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137438957552L) != 0)) {
				{
				setState(112);
				parameterList();
				}
			}

			setState(115);
			match(RPAREN);
			setState(116);
			match(LBRACE);
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137438961648L) != 0)) {
				{
				{
				setState(117);
				statement();
				}
				}
				setState(122);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(123);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterListContext extends ParserRuleContext {
		public List<VariableDeclarationContext> variableDeclaration() {
			return getRuleContexts(VariableDeclarationContext.class);
		}
		public VariableDeclarationContext variableDeclaration(int i) {
			return getRuleContext(VariableDeclarationContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CppParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CppParser.COMMA, i);
		}
		public ParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterList; }
	}

	public final ParameterListContext parameterList() throws RecognitionException {
		ParameterListContext _localctx = new ParameterListContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_parameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			variableDeclaration();
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(126);
				match(COMMA);
				setState(127);
				variableDeclaration();
				}
				}
				setState(132);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode VOID() { return getToken(CppParser.VOID, 0); }
		public TerminalNode STRING() { return getToken(CppParser.STRING, 0); }
		public TerminalNode CHAR() { return getToken(CppParser.CHAR, 0); }
		public TerminalNode INT() { return getToken(CppParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(CppParser.FLOAT, 0); }
		public TerminalNode DOUBLE() { return getToken(CppParser.DOUBLE, 0); }
		public TerminalNode BOOL() { return getToken(CppParser.BOOL, 0); }
		public TerminalNode ID() { return getToken(CppParser.ID, 0); }
		public TerminalNode STD() { return getToken(CppParser.STD, 0); }
		public TerminalNode COLONCOLON() { return getToken(CppParser.COLONCOLON, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STD) {
				{
				setState(133);
				match(STD);
				setState(134);
				match(COLONCOLON);
				}
			}

			setState(137);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 137438955504L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VariableDeclarationContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(CppParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(CppParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public VariableDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableDeclaration; }
	}

	public final VariableDeclarationContext variableDeclaration() throws RecognitionException {
		VariableDeclarationContext _localctx = new VariableDeclarationContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_variableDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			type();
			setState(140);
			match(ID);
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(141);
				match(ASSIGN);
				setState(142);
				expression();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public MethodCallContext methodCall() {
			return getRuleContext(MethodCallContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(CppParser.SEMI, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public ObjectDeclarationContext objectDeclaration() {
			return getRuleContext(ObjectDeclarationContext.class,0);
		}
		public AssignementContext assignement() {
			return getRuleContext(AssignementContext.class,0);
		}
		public VariableDeclarationContext variableDeclaration() {
			return getRuleContext(VariableDeclarationContext.class,0);
		}
		public TerminalNode RETURN() { return getToken(CppParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_statement);
		int _la;
		try {
			setState(165);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(145);
				methodCall();
				setState(146);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(148);
				functionCall();
				setState(149);
				match(SEMI);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(151);
				objectDeclaration();
				setState(152);
				match(SEMI);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(154);
				assignement();
				setState(155);
				match(SEMI);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(157);
				variableDeclaration();
				setState(158);
				match(SEMI);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(160);
				match(RETURN);
				setState(162);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 962073722880L) != 0)) {
					{
					setState(161);
					expression();
					}
				}

				setState(164);
				match(SEMI);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MethodCallContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(CppParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(CppParser.ID, i);
		}
		public TerminalNode DOT() { return getToken(CppParser.DOT, 0); }
		public TerminalNode LPAREN() { return getToken(CppParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CppParser.RPAREN, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public MethodCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodCall; }
	}

	public final MethodCallContext methodCall() throws RecognitionException {
		MethodCallContext _localctx = new MethodCallContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_methodCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(ID);
			setState(168);
			match(DOT);
			setState(169);
			match(ID);
			setState(170);
			match(LPAREN);
			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 962073722880L) != 0)) {
				{
				setState(171);
				argumentList();
				}
			}

			setState(174);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CppParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CppParser.COMMA, i);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			expression();
			setState(181);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(177);
				match(COMMA);
				setState(178);
				expression();
				}
				}
				setState(183);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CppParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(CppParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(CppParser.RPAREN, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			match(ID);
			setState(185);
			match(LPAREN);
			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 962073722880L) != 0)) {
				{
				setState(186);
				argumentList();
				}
			}

			setState(189);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ShiftExpressionContext shiftExpression() {
			return getRuleContext(ShiftExpressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			shiftExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ShiftExpressionContext extends ParserRuleContext {
		public List<AdditiveExpressionContext> additiveExpression() {
			return getRuleContexts(AdditiveExpressionContext.class);
		}
		public AdditiveExpressionContext additiveExpression(int i) {
			return getRuleContext(AdditiveExpressionContext.class,i);
		}
		public List<TerminalNode> LEFT_SHIFT() { return getTokens(CppParser.LEFT_SHIFT); }
		public TerminalNode LEFT_SHIFT(int i) {
			return getToken(CppParser.LEFT_SHIFT, i);
		}
		public ShiftExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shiftExpression; }
	}

	public final ShiftExpressionContext shiftExpression() throws RecognitionException {
		ShiftExpressionContext _localctx = new ShiftExpressionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_shiftExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			additiveExpression();
			setState(198);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LEFT_SHIFT) {
				{
				{
				setState(194);
				match(LEFT_SHIFT);
				setState(195);
				additiveExpression();
				}
				}
				setState(200);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AdditiveExpressionContext extends ParserRuleContext {
		public List<MultiplicativeExpressionContext> multiplicativeExpression() {
			return getRuleContexts(MultiplicativeExpressionContext.class);
		}
		public MultiplicativeExpressionContext multiplicativeExpression(int i) {
			return getRuleContext(MultiplicativeExpressionContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(CppParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(CppParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(CppParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(CppParser.MINUS, i);
		}
		public AdditiveExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additiveExpression; }
	}

	public final AdditiveExpressionContext additiveExpression() throws RecognitionException {
		AdditiveExpressionContext _localctx = new AdditiveExpressionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_additiveExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			multiplicativeExpression();
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(202);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(203);
				multiplicativeExpression();
				}
				}
				setState(208);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicativeExpressionContext extends ParserRuleContext {
		public List<PostfixExpressionContext> postfixExpression() {
			return getRuleContexts(PostfixExpressionContext.class);
		}
		public PostfixExpressionContext postfixExpression(int i) {
			return getRuleContext(PostfixExpressionContext.class,i);
		}
		public List<TerminalNode> STAR() { return getTokens(CppParser.STAR); }
		public TerminalNode STAR(int i) {
			return getToken(CppParser.STAR, i);
		}
		public List<TerminalNode> DIV() { return getTokens(CppParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(CppParser.DIV, i);
		}
		public MultiplicativeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicativeExpression; }
	}

	public final MultiplicativeExpressionContext multiplicativeExpression() throws RecognitionException {
		MultiplicativeExpressionContext _localctx = new MultiplicativeExpressionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_multiplicativeExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			postfixExpression();
			setState(214);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==STAR || _la==DIV) {
				{
				{
				setState(210);
				_la = _input.LA(1);
				if ( !(_la==STAR || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(211);
				postfixExpression();
				}
				}
				setState(216);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PostfixExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public List<PostfixOpContext> postfixOp() {
			return getRuleContexts(PostfixOpContext.class);
		}
		public PostfixOpContext postfixOp(int i) {
			return getRuleContext(PostfixOpContext.class,i);
		}
		public PostfixExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_postfixExpression; }
	}

	public final PostfixExpressionContext postfixExpression() throws RecognitionException {
		PostfixExpressionContext _localctx = new PostfixExpressionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_postfixExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			primaryExpression();
			setState(221);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT || _la==COLONCOLON) {
				{
				{
				setState(218);
				postfixOp();
				}
				}
				setState(223);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PostfixOpContext extends ParserRuleContext {
		public TerminalNode COLONCOLON() { return getToken(CppParser.COLONCOLON, 0); }
		public TerminalNode ID() { return getToken(CppParser.ID, 0); }
		public TerminalNode DOT() { return getToken(CppParser.DOT, 0); }
		public PostfixOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_postfixOp; }
	}

	public final PostfixOpContext postfixOp() throws RecognitionException {
		PostfixOpContext _localctx = new PostfixOpContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_postfixOp);
		try {
			setState(228);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COLONCOLON:
				enterOuterAlt(_localctx, 1);
				{
				setState(224);
				match(COLONCOLON);
				setState(225);
				match(ID);
				}
				break;
			case DOT:
				enterOuterAlt(_localctx, 2);
				{
				setState(226);
				match(DOT);
				setState(227);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryExpressionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CppParser.ID, 0); }
		public TerminalNode STRING_LITERAL() { return getToken(CppParser.STRING_LITERAL, 0); }
		public TerminalNode NUMBER() { return getToken(CppParser.NUMBER, 0); }
		public TerminalNode LPAREN() { return getToken(CppParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(CppParser.RPAREN, 0); }
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_primaryExpression);
		try {
			setState(237);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(230);
				match(ID);
				}
				break;
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(231);
				match(STRING_LITERAL);
				}
				break;
			case NUMBER:
				enterOuterAlt(_localctx, 3);
				{
				setState(232);
				match(NUMBER);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 4);
				{
				setState(233);
				match(LPAREN);
				setState(234);
				expression();
				setState(235);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignementContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CppParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(CppParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignement; }
	}

	public final AssignementContext assignement() throws RecognitionException {
		AssignementContext _localctx = new AssignementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_assignement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			match(ID);
			setState(240);
			match(ASSIGN);
			setState(241);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ObjectDeclarationContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(CppParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(CppParser.ID, i);
		}
		public ObjectDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_objectDeclaration; }
	}

	public final ObjectDeclarationContext objectDeclaration() throws RecognitionException {
		ObjectDeclarationContext _localctx = new ObjectDeclarationContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_objectDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			match(ID);
			setState(244);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001*\u00f7\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0005\u00005\b\u0000\n\u0000\f\u00008\t\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0005\u0003I\b\u0003\n\u0003\f\u0003"+
		"L\t\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004S\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005Y\b\u0005\u0001\u0006\u0003\u0006\\\b\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0003\u0006b\b\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0005\u0006g\b\u0006\n\u0006\f\u0006j\t\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003"+
		"\u0007r\b\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007w\b\u0007"+
		"\n\u0007\f\u0007z\t\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0005\b\u0081\b\b\n\b\f\b\u0084\t\b\u0001\t\u0001\t\u0003\t\u0088\b"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u0090\b\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u00a3"+
		"\b\u000b\u0001\u000b\u0003\u000b\u00a6\b\u000b\u0001\f\u0001\f\u0001\f"+
		"\u0001\f\u0001\f\u0003\f\u00ad\b\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0005\r\u00b4\b\r\n\r\f\r\u00b7\t\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0003\u000e\u00bc\b\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u00c5\b\u0010\n\u0010"+
		"\f\u0010\u00c8\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011"+
		"\u00cd\b\u0011\n\u0011\f\u0011\u00d0\t\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0005\u0012\u00d5\b\u0012\n\u0012\f\u0012\u00d8\t\u0012\u0001\u0013"+
		"\u0001\u0013\u0005\u0013\u00dc\b\u0013\n\u0013\f\u0013\u00df\t\u0013\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u00e5\b\u0014\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0003\u0015\u00ee\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0000\u0000\u0018"+
		"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u001c\u001e \"$&(*,.\u0000\u0003\u0002\u0000\u0004\n%%\u0001\u0000\u001a"+
		"\u001b\u0001\u0000\u001c\u001d\u00ff\u00006\u0001\u0000\u0000\u0000\u0002"+
		";\u0001\u0000\u0000\u0000\u0004@\u0001\u0000\u0000\u0000\u0006J\u0001"+
		"\u0000\u0000\u0000\bR\u0001\u0000\u0000\u0000\nX\u0001\u0000\u0000\u0000"+
		"\f[\u0001\u0000\u0000\u0000\u000em\u0001\u0000\u0000\u0000\u0010}\u0001"+
		"\u0000\u0000\u0000\u0012\u0087\u0001\u0000\u0000\u0000\u0014\u008b\u0001"+
		"\u0000\u0000\u0000\u0016\u00a5\u0001\u0000\u0000\u0000\u0018\u00a7\u0001"+
		"\u0000\u0000\u0000\u001a\u00b0\u0001\u0000\u0000\u0000\u001c\u00b8\u0001"+
		"\u0000\u0000\u0000\u001e\u00bf\u0001\u0000\u0000\u0000 \u00c1\u0001\u0000"+
		"\u0000\u0000\"\u00c9\u0001\u0000\u0000\u0000$\u00d1\u0001\u0000\u0000"+
		"\u0000&\u00d9\u0001\u0000\u0000\u0000(\u00e4\u0001\u0000\u0000\u0000*"+
		"\u00ed\u0001\u0000\u0000\u0000,\u00ef\u0001\u0000\u0000\u0000.\u00f3\u0001"+
		"\u0000\u0000\u000005\u0003\u0002\u0001\u000015\u0003\u0004\u0002\u0000"+
		"25\u0003\u000e\u0007\u000035\u0003\u0016\u000b\u000040\u0001\u0000\u0000"+
		"\u000041\u0001\u0000\u0000\u000042\u0001\u0000\u0000\u000043\u0001\u0000"+
		"\u0000\u000058\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u000067\u0001"+
		"\u0000\u0000\u000079\u0001\u0000\u0000\u000086\u0001\u0000\u0000\u0000"+
		"9:\u0005\u0000\u0000\u0001:\u0001\u0001\u0000\u0000\u0000;<\u0005\u0011"+
		"\u0000\u0000<=\u0005#\u0000\u0000=>\u0005%\u0000\u0000>?\u0005$\u0000"+
		"\u0000?\u0003\u0001\u0000\u0000\u0000@A\u0005\u0001\u0000\u0000AB\u0005"+
		"%\u0000\u0000BC\u0005\u0012\u0000\u0000CD\u0003\u0006\u0003\u0000DE\u0005"+
		"\u0013\u0000\u0000EF\u0005\u0016\u0000\u0000F\u0005\u0001\u0000\u0000"+
		"\u0000GI\u0003\b\u0004\u0000HG\u0001\u0000\u0000\u0000IL\u0001\u0000\u0000"+
		"\u0000JH\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000K\u0007\u0001"+
		"\u0000\u0000\u0000LJ\u0001\u0000\u0000\u0000MS\u0003\n\u0005\u0000NS\u0003"+
		"\f\u0006\u0000OP\u0003\u0014\n\u0000PQ\u0005\u0016\u0000\u0000QS\u0001"+
		"\u0000\u0000\u0000RM\u0001\u0000\u0000\u0000RN\u0001\u0000\u0000\u0000"+
		"RO\u0001\u0000\u0000\u0000S\t\u0001\u0000\u0000\u0000TU\u0005\u0002\u0000"+
		"\u0000UY\u0005\u001f\u0000\u0000VW\u0005\u0003\u0000\u0000WY\u0005\u001f"+
		"\u0000\u0000XT\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000Y\u000b"+
		"\u0001\u0000\u0000\u0000Z\\\u0005\u0002\u0000\u0000[Z\u0001\u0000\u0000"+
		"\u0000[\\\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]^\u0003\u0012"+
		"\t\u0000^_\u0005%\u0000\u0000_a\u0005\u0014\u0000\u0000`b\u0003\u0010"+
		"\b\u0000a`\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000bc\u0001\u0000"+
		"\u0000\u0000cd\u0005\u0015\u0000\u0000dh\u0005\u0012\u0000\u0000eg\u0003"+
		"\u0016\u000b\u0000fe\u0001\u0000\u0000\u0000gj\u0001\u0000\u0000\u0000"+
		"hf\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ik\u0001\u0000\u0000"+
		"\u0000jh\u0001\u0000\u0000\u0000kl\u0005\u0013\u0000\u0000l\r\u0001\u0000"+
		"\u0000\u0000mn\u0003\u0012\t\u0000no\u0005%\u0000\u0000oq\u0005\u0014"+
		"\u0000\u0000pr\u0003\u0010\b\u0000qp\u0001\u0000\u0000\u0000qr\u0001\u0000"+
		"\u0000\u0000rs\u0001\u0000\u0000\u0000st\u0005\u0015\u0000\u0000tx\u0005"+
		"\u0012\u0000\u0000uw\u0003\u0016\u000b\u0000vu\u0001\u0000\u0000\u0000"+
		"wz\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000"+
		"\u0000y{\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000{|\u0005\u0013"+
		"\u0000\u0000|\u000f\u0001\u0000\u0000\u0000}\u0082\u0003\u0014\n\u0000"+
		"~\u007f\u0005\u0017\u0000\u0000\u007f\u0081\u0003\u0014\n\u0000\u0080"+
		"~\u0001\u0000\u0000\u0000\u0081\u0084\u0001\u0000\u0000\u0000\u0082\u0080"+
		"\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0011"+
		"\u0001\u0000\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0086"+
		"\u0005\u000b\u0000\u0000\u0086\u0088\u0005 \u0000\u0000\u0087\u0085\u0001"+
		"\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u0089\u0001"+
		"\u0000\u0000\u0000\u0089\u008a\u0007\u0000\u0000\u0000\u008a\u0013\u0001"+
		"\u0000\u0000\u0000\u008b\u008c\u0003\u0012\t\u0000\u008c\u008f\u0005%"+
		"\u0000\u0000\u008d\u008e\u0005\u0019\u0000\u0000\u008e\u0090\u0003\u001e"+
		"\u000f\u0000\u008f\u008d\u0001\u0000\u0000\u0000\u008f\u0090\u0001\u0000"+
		"\u0000\u0000\u0090\u0015\u0001\u0000\u0000\u0000\u0091\u0092\u0003\u0018"+
		"\f\u0000\u0092\u0093\u0005\u0016\u0000\u0000\u0093\u00a6\u0001\u0000\u0000"+
		"\u0000\u0094\u0095\u0003\u001c\u000e\u0000\u0095\u0096\u0005\u0016\u0000"+
		"\u0000\u0096\u00a6\u0001\u0000\u0000\u0000\u0097\u0098\u0003.\u0017\u0000"+
		"\u0098\u0099\u0005\u0016\u0000\u0000\u0099\u00a6\u0001\u0000\u0000\u0000"+
		"\u009a\u009b\u0003,\u0016\u0000\u009b\u009c\u0005\u0016\u0000\u0000\u009c"+
		"\u00a6\u0001\u0000\u0000\u0000\u009d\u009e\u0003\u0014\n\u0000\u009e\u009f"+
		"\u0005\u0016\u0000\u0000\u009f\u00a6\u0001\u0000\u0000\u0000\u00a0\u00a2"+
		"\u0005\f\u0000\u0000\u00a1\u00a3\u0003\u001e\u000f\u0000\u00a2\u00a1\u0001"+
		"\u0000\u0000\u0000\u00a2\u00a3\u0001\u0000\u0000\u0000\u00a3\u00a4\u0001"+
		"\u0000\u0000\u0000\u00a4\u00a6\u0005\u0016\u0000\u0000\u00a5\u0091\u0001"+
		"\u0000\u0000\u0000\u00a5\u0094\u0001\u0000\u0000\u0000\u00a5\u0097\u0001"+
		"\u0000\u0000\u0000\u00a5\u009a\u0001\u0000\u0000\u0000\u00a5\u009d\u0001"+
		"\u0000\u0000\u0000\u00a5\u00a0\u0001\u0000\u0000\u0000\u00a6\u0017\u0001"+
		"\u0000\u0000\u0000\u00a7\u00a8\u0005%\u0000\u0000\u00a8\u00a9\u0005\u0018"+
		"\u0000\u0000\u00a9\u00aa\u0005%\u0000\u0000\u00aa\u00ac\u0005\u0014\u0000"+
		"\u0000\u00ab\u00ad\u0003\u001a\r\u0000\u00ac\u00ab\u0001\u0000\u0000\u0000"+
		"\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000"+
		"\u00ae\u00af\u0005\u0015\u0000\u0000\u00af\u0019\u0001\u0000\u0000\u0000"+
		"\u00b0\u00b5\u0003\u001e\u000f\u0000\u00b1\u00b2\u0005\u0017\u0000\u0000"+
		"\u00b2\u00b4\u0003\u001e\u000f\u0000\u00b3\u00b1\u0001\u0000\u0000\u0000"+
		"\u00b4\u00b7\u0001\u0000\u0000\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000"+
		"\u00b5\u00b6\u0001\u0000\u0000\u0000\u00b6\u001b\u0001\u0000\u0000\u0000"+
		"\u00b7\u00b5\u0001\u0000\u0000\u0000\u00b8\u00b9\u0005%\u0000\u0000\u00b9"+
		"\u00bb\u0005\u0014\u0000\u0000\u00ba\u00bc\u0003\u001a\r\u0000\u00bb\u00ba"+
		"\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00bd"+
		"\u0001\u0000\u0000\u0000\u00bd\u00be\u0005\u0015\u0000\u0000\u00be\u001d"+
		"\u0001\u0000\u0000\u0000\u00bf\u00c0\u0003 \u0010\u0000\u00c0\u001f\u0001"+
		"\u0000\u0000\u0000\u00c1\u00c6\u0003\"\u0011\u0000\u00c2\u00c3\u0005!"+
		"\u0000\u0000\u00c3\u00c5\u0003\"\u0011\u0000\u00c4\u00c2\u0001\u0000\u0000"+
		"\u0000\u00c5\u00c8\u0001\u0000\u0000\u0000\u00c6\u00c4\u0001\u0000\u0000"+
		"\u0000\u00c6\u00c7\u0001\u0000\u0000\u0000\u00c7!\u0001\u0000\u0000\u0000"+
		"\u00c8\u00c6\u0001\u0000\u0000\u0000\u00c9\u00ce\u0003$\u0012\u0000\u00ca"+
		"\u00cb\u0007\u0001\u0000\u0000\u00cb\u00cd\u0003$\u0012\u0000\u00cc\u00ca"+
		"\u0001\u0000\u0000\u0000\u00cd\u00d0\u0001\u0000\u0000\u0000\u00ce\u00cc"+
		"\u0001\u0000\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf#\u0001"+
		"\u0000\u0000\u0000\u00d0\u00ce\u0001\u0000\u0000\u0000\u00d1\u00d6\u0003"+
		"&\u0013\u0000\u00d2\u00d3\u0007\u0002\u0000\u0000\u00d3\u00d5\u0003&\u0013"+
		"\u0000\u00d4\u00d2\u0001\u0000\u0000\u0000\u00d5\u00d8\u0001\u0000\u0000"+
		"\u0000\u00d6\u00d4\u0001\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000"+
		"\u0000\u00d7%\u0001\u0000\u0000\u0000\u00d8\u00d6\u0001\u0000\u0000\u0000"+
		"\u00d9\u00dd\u0003*\u0015\u0000\u00da\u00dc\u0003(\u0014\u0000\u00db\u00da"+
		"\u0001\u0000\u0000\u0000\u00dc\u00df\u0001\u0000\u0000\u0000\u00dd\u00db"+
		"\u0001\u0000\u0000\u0000\u00dd\u00de\u0001\u0000\u0000\u0000\u00de\'\u0001"+
		"\u0000\u0000\u0000\u00df\u00dd\u0001\u0000\u0000\u0000\u00e0\u00e1\u0005"+
		" \u0000\u0000\u00e1\u00e5\u0005%\u0000\u0000\u00e2\u00e3\u0005\u0018\u0000"+
		"\u0000\u00e3\u00e5\u0005%\u0000\u0000\u00e4\u00e0\u0001\u0000\u0000\u0000"+
		"\u00e4\u00e2\u0001\u0000\u0000\u0000\u00e5)\u0001\u0000\u0000\u0000\u00e6"+
		"\u00ee\u0005%\u0000\u0000\u00e7\u00ee\u0005\'\u0000\u0000\u00e8\u00ee"+
		"\u0005&\u0000\u0000\u00e9\u00ea\u0005\u0014\u0000\u0000\u00ea\u00eb\u0003"+
		"\u001e\u000f\u0000\u00eb\u00ec\u0005\u0015\u0000\u0000\u00ec\u00ee\u0001"+
		"\u0000\u0000\u0000\u00ed\u00e6\u0001\u0000\u0000\u0000\u00ed\u00e7\u0001"+
		"\u0000\u0000\u0000\u00ed\u00e8\u0001\u0000\u0000\u0000\u00ed\u00e9\u0001"+
		"\u0000\u0000\u0000\u00ee+\u0001\u0000\u0000\u0000\u00ef\u00f0\u0005%\u0000"+
		"\u0000\u00f0\u00f1\u0005\u0019\u0000\u0000\u00f1\u00f2\u0003\u001e\u000f"+
		"\u0000\u00f2-\u0001\u0000\u0000\u0000\u00f3\u00f4\u0005%\u0000\u0000\u00f4"+
		"\u00f5\u0005%\u0000\u0000\u00f5/\u0001\u0000\u0000\u0000\u001846JRX[a"+
		"hqx\u0082\u0087\u008f\u00a2\u00a5\u00ac\u00b5\u00bb\u00c6\u00ce\u00d6"+
		"\u00dd\u00e4\u00ed";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}