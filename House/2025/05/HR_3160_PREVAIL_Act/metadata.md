# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3160?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3160
- Title: PREVAIL Act
- Congress: 119
- Bill type: HR
- Bill number: 3160
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-02-03T14:34:42Z
- Update date including text: 2026-02-03T14:34:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3160",
    "number": "3160",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001224",
        "district": "1",
        "firstName": "Nathaniel",
        "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
        "lastName": "Moran",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "PREVAIL Act",
    "type": "HR",
    "updateDate": "2026-02-03T14:34:42Z",
    "updateDateIncludingText": "2026-02-03T14:34:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-05-01T13:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NC"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3160ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3160\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Moran (for himself and Ms. Ross ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 35, United States Code, to invest in inventors in the United States, maintain the United States as the leading innovation economy in the world, and protect the property rights of the inventors that grow the economy of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting and Respecting Economically Vital American Innovation Leadership Act or the PREVAIL Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe patent property rights enshrined in the Constitution of the United States provide the foundation for the exceptional innovation environment in the United States.\n**(2)**\nReliable and effective patent protection encourages United States inventors to invest their resources in creating new inventions.\n**(3)**\nUnited States inventors have made discoveries leading to patient cures, positive changes to the standard of living for all people in the United States, and improvements to the agricultural, telecommunications, and electronics industries, among others.\n**(4)**\nThe United States patent system is an essential part of the economic success of the United States.\n**(5)**\nReliable and effective patent protection improves the chances of success for individual inventors and small companies and increases the chances of securing investments for those inventors and companies.\n**(6)**\nIntellectual property-intensive industries in the United States\u2014\n**(A)**\ngenerate tens of millions of jobs for individuals in the United States; and\n**(B)**\naccount for more than 1/3 of the gross domestic product of the United States.\n**(7)**\nThe National Security Commission on Artificial Intelligence has emphasized that\u2014\n**(A)**\nthe People\u2019s Republic of China is leveraging and exploiting intellectual property as a critical tool within its national strategies for emerging technologies; and\n**(B)**\nthe United States has failed to similarly recognize the importance of intellectual property in securing its own national security, economic interests, and technological competitiveness.\n**(8)**\nIn the highly competitive global economy, the United States needs reliable and effective patent protections to safeguard national security interests and maintain its position as the most innovative country in the world.\n**(9)**\nCongress last enacted comprehensive reforms of the patent system in 2011.\n**(10)**\nUnintended consequences of the comprehensive 2011 reform of patent laws have become evident during the decade preceding the date of enactment of this Act, including the strategic filing of post-grant review proceedings to depress stock prices and extort settlements, the filing of repetitive petitions for inter partes and post-grant reviews that have the effect of harassing patent owners, and the unnecessary duplication of work by the district courts of the United States and the Patent Trial and Appeal Board, all of which drive down investment in innovation and frustrate the purpose of those patent reform laws.\n**(11)**\nEfforts by Congress to reform the patent system without careful scrutiny create a serious risk of making it more costly and difficult for innovators to protect their patents from infringement, thereby\u2014\n**(A)**\ndisincentivizing United States companies from innovating; and\n**(B)**\nweakening the economy of the United States.\n#### 3. Patent trial and appeal board\nSection 6 of title 35, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (b), (c), and (d) as subsections (c), (d), and (e), respectively;\n**(2)**\nby inserting after subsection (a) the following:\n(b) Code of conduct (1) In general The Director shall prescribe regulations establishing a code of conduct for the members of the Patent Trial and Appeal Board. (2) Considerations In prescribing regulations under paragraph (1), the Director shall consider the Code of Conduct for United States Judges and how the provisions of that Code of Conduct may apply to the Patent Trial and Appeal Board. ;\n**(3)**\nby striking subsection (d), as so redesignated, and inserting the following:\n(d) 3-Member panels (1) In general Each appeal, derivation proceeding, post-grant review, and inter partes review shall be heard by at least 3 members of the Patent Trial and Appeal Board, who shall be designated by the Director. The Patent Trial and Appeal Board may grant rehearings. (2) Changes to constitution of panel After the constitution of a panel of the Patent Trial and Appeal Board under this subsection has been made public, any changes to the constitution of that panel, including changes that were made before the constitution of the panel was made public, shall be noted in the record. (3) No direction or influence An officer who has supervisory authority or disciplinary authority with respect to an administrative patent judge of the Patent Trial and Appeal Board (or a delegate of such an officer), and who is not a member of a panel described in this subsection, shall refrain from communications with the panel that direct or otherwise influence any merits decision of the panel. (4) Ineligibility to hear review A member of the Patent Trial and Appeal Board who participates in the decision to institute an inter partes review or a post-grant review of a patent shall be ineligible to hear the review. ; and\n**(4)**\nin subsection (e), as so redesignated\u2014\n**(A)**\nin the first sentence\u2014\n**(i)**\nby striking the date of the enactment of this subsection and inserting the date of enactment of the Promoting and Respecting Economically Vital American Innovation Leadership Act ;\n**(ii)**\nby striking by the Director and inserting by the Director or the Secretary ; and\n**(iii)**\nby inserting or the Secretary, as applicable, after on which the Director ; and\n**(B)**\nin the second sentence\u2014\n**(i)**\nby inserting after by the Director the following: , or, before the date of enactment of the Promoting and Respecting Economically Vital American Innovation Leadership Act , having performed duties no longer performed by administrative patent judges, ; and\n**(ii)**\nby striking that the administrative patent judge so appointed and inserting that the applicable administrative patent judge .\n#### 4. Inter partes review\n##### (a) Real parties in interest\nSection 311 of title 35, United States Code, is amended by adding at the end the following:\n(d) Real party in interest For purposes of this chapter, a person that, directly or through an affiliate, subsidiary, or proxy, makes a financial contribution to the preparation for, or conduct during, an inter partes review on behalf of a petitioner shall be considered a real party in interest of that petitioner. .\n##### (b) Petitioner certification and Director determination\nSection 312(a) of title 35, United States Code, is amended\u2014\n**(1)**\nin paragraph (4), by striking and at the end;\n**(2)**\nin paragraph (5), by striking the period at the end and inserting and ; and\n**(3)**\nby adding at the end the following:\n(6) the petitioner certifies, and the Director determines, that the petitioner\u2014 (A) is a nonprofit organization that\u2014 (i) is exempt from taxation under section 501(a) of the Internal Revenue Code of 1986, described in section 501(c)(3) of such Code, and described in section 170(b)(1)(A) of such Code, other than an organization described in section 509(a)(3) of such Code; (ii) does not have any member, donor, or other funding source that is, or reasonably could be accused of, infringing 1 or more claims of the challenged patent; and (iii) is filing the petition for the sole purpose of ascertaining the patentability of the challenged claims of the patent and not to profit from or fund the operations of the petitioner; (B) is currently engaging in, or has a bona fide intent to engage in, conduct within the United States that reasonably could be accused of infringing 1 or more claims of the challenged patent; (C) would have standing to bring a civil action in a court of the United States seeking a declaratory judgment of invalidity with respect to 1 or more claims of the challenged patent; or (D) has been sued in a court of the United States for infringement of the challenged patent. .\n##### (c) Institution decision rehearing timing\nSection 314 of title 35, United States Code, is amended by adding at the end the following:\n(e) Rehearing Not later than 45 days after the date on which a request for rehearing from a determination by the Director under subsection (b) is filed, the Director shall finally decide any request for reconsideration, rehearing, or review with respect to the determination, except that the Director may, for good cause shown, extend that 45-day period by not more than 30 days. .\n##### (d) Eliminating repetitive proceedings\n**(1) In general**\nSection 315 of title 35, United States Code, is amended\u2014\n**(A)**\nin subsection (b), by amending the second sentence to read as follows: The time limitation set forth in the preceding sentence shall not bar a request for joinder under subsection (d), but shall establish a rebuttable presumption against joinder for the requesting person. ;\n**(B)**\nby redesignating subsections (c), (d), and (e) as subsections (d), (e), and (f), respectively;\n**(C)**\nby inserting after subsection (b) the following:\n(c) Single forum (1) In general If an inter partes review is instituted challenging the validity of a patent, the petitioner, a real party in interest, or a privy of the petitioner may not file or maintain, in a civil action arising in whole or in part under section 1338 of title 28, or in a proceeding before the International Trade Commission under section 337 of the Tariff Act of 1930 ( 19 U.S.C. 1337 ), a claim, a counterclaim, or an affirmative defense challenging the validity of any claim of the patent on any ground described in section 311(b). (2) Considerations In determining whether to institute a proceeding under this chapter, subject to the provisions of subsections (a)(1) and (g), the Director may not reject a petition requesting an inter partes review on the basis of the petitioner, a real party in interest, or a privy of the petitioner filing or maintaining a claim, a counterclaim, or an affirmative defense challenging the validity of the applicable patent in any civil action arising in whole or in part under section 1338 of title 28, or in a proceeding before the International Trade Commission under section 337 of the Tariff Act of 1930 ( 19 U.S.C. 1337 ). ;\n**(D)**\nby amending subsection (d), as so redesignated, to read as follows:\n(d) Joinder (1) In general If the Director institutes an inter partes review, the Director, in the discretion of the Director, may join as a party to that inter partes review any person that properly files a request to join the inter partes review and a petition under section 311 that the Director, after receiving a preliminary response under section 313 or the expiration of the time for filing such a response, determines warrants the institution of an inter partes review under section 314. (2) Time-barred person Pursuant to paragraph (1), the Director, in the discretion of the Director, may join as a party to an inter partes review a person that did not satisfy the time limitation under subsection (b) that rebuts the presumption against joinder, except that any such person shall not be permitted to serve as the lead petitioner and shall not be permitted to maintain the inter partes review unless a petitioner that satisfied the time limitation under subsection (b) remains in the inter partes review. ;\n**(E)**\nby amending subsection (e), as so redesignated, to read as follows:\n(e) Multiple proceedings (1) In general Notwithstanding sections 135(a), 251, and 252, and chapter 30, after a petition to institute an inter partes review is filed, if another proceeding or matter involving the patent is before the Office\u2014 (A) the parties shall notify the Director of that other proceeding or matter\u2014 (i) not later than 30 days after the date of entry of the notice of filing date accorded to the petition; or (ii) if the other proceeding or matter is filed after the date on which the petition to institute an inter partes review is filed, not later than 30 days after the date on which the other proceeding or matter is filed; and (B) the Director shall issue a decision determining the manner in which the inter partes review or other proceeding or matter may proceed, including providing for stay, transfer, consolidation, or termination of any such matter or proceeding. (2) Considerations In determining whether to institute a proceeding under this chapter, the Director shall, unless the Director determines that the petitioner has demonstrated exceptional circumstances, reject any petition that presents prior art or an argument that is the same or substantially the same as prior art or an argument that previously was presented to the Office. ;\n**(F)**\nby amending subsection (f), as so redesignated, to read as follows:\n(f) Estoppel (1) In general A petitioner that has previously requested an inter partes review of a claim in a patent under this chapter, or a real party in interest or a privy of such a petitioner, may not request or maintain another proceeding before the Office with respect to that patent on any ground that the petitioner raised or reasonably could have raised in the petition requesting or during the prior inter partes review, unless\u2014 (A) after the filing of the initial petition, the petitioner, or a real party in interest or a privy of the petitioner, is charged with infringement of additional claims of the patent; (B) a subsequent petition requests an inter partes review of only the additional claims of the patent that the petitioner, or a real party in interest or a privy of the petitioner, is later charged with infringing; and (C) that subsequent petition is accompanied by a request for joinder to the prior inter partes review, which overcomes the rebuttable presumption against joinder set forth in subsection (b), and which the Director shall grant if the Director authorizes an inter partes review to be instituted on the subsequent petition under section 314. (2) Joined party Any person joined as a party to an inter partes review, and any real party in interest or any privy of such person, shall be estopped under this subsection and subsections (c)(1) and (e)(2) to the same extent as if that person, real party in interest, or privy had been the first petitioner in that inter partes review. ; and\n**(G)**\nby adding at the end the following:\n(g) Federal court and International Trade Commission validity determinations An inter partes review of a patent claim may not be instituted or maintained if, in a civil action arising in whole or in part under section 1338 of title 28, or in a proceeding before the International Trade Commission under section 337 of the Tariff Act of 1930 ( 19 U.S.C. 1337 ), in which the petitioner, a real party in interest, or a privy of the petitioner is a party, the court, or the International Trade Commission, as applicable, has entered a final judgment that decides a challenge to the validity of the patent claim with respect to any ground described in section 311(b). .\n**(2) Technical and conforming amendments**\nSection 316(a) of title 35, United States Code, is amended\u2014\n**(A)**\nin paragraph (11), by striking section 315(c) and inserting section 315(d) ; and\n**(B)**\nin paragraph (12), by striking section 315(c) and inserting section 315(d) .\n##### (e) Conduct of inter partes review\nSection 316 of title 35, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (2) through (13) as paragraphs (3) through (14), respectively;\n**(B)**\nby inserting after paragraph (1) the following:\n(2) establishing procedures for briefing and limited discovery, at the request and discretion of the Director, for assisting the Director in making a determination under section 312(a)(6); ;\n**(C)**\nby amending paragraph (6), as so redesignated, to read as follows:\n(6) setting forth standards and procedures for discovery of relevant evidence, including that such discovery shall be limited to\u2014 (A) the deposition of witnesses submitting affidavits or declarations; (B) evidence identifying the real parties in interest of the petitioner; and (C) what is otherwise necessary in the interest of justice; ;\n**(D)**\nby amending paragraph (10), as so redesignated, to read as follows:\n(10) setting forth standards and procedures for\u2014 (A) allowing the patent owner to move to amend the patent under subsection (d) to cancel a challenged claim or propose a reasonable number of substitute claims; (B) allowing the Patent Trial and Appeal Board to provide guidance on substitute claims proposed by the patent owner; (C) allowing the patent owner to further revise proposed substitute claims after the issuance of guidance described in subparagraph (B); and (D) ensuring that any information submitted by the patent owner in support of any amendment entered under subsection (d), and any guidance issued by the Patent Trial and Appeal Board, is made available to the public as part of the prosecution history of the patent; ;\n**(E)**\nin paragraph (13), as so redesignated, by striking and at the end;\n**(F)**\nin paragraph (14), as so redesignated, by striking the period at the end and inserting ; and ; and\n**(G)**\nby adding at the end the following:\n(15) setting forth the standards for demonstrating exceptional circumstances under sections 303(e)(1) and 315(e)(2). ;\n**(2)**\nby amending subsection (e) to read as follows:\n(e) Evidentiary standards (1) Presumption of validity The presumption of validity under section 282(a) shall apply to previously issued claims of a patent that is challenged in an inter partes review under this chapter. (2) Burden of proof In an inter partes review under this chapter\u2014 (A) the petitioner shall have the burden of proving a proposition of unpatentability of a previously issued claim of a patent by clear and convincing evidence; and (B) the petitioner shall have the burden of persuasion, by a preponderance of the evidence, with respect to a proposition of unpatentability for any substitute claim proposed by the patent owner. ; and\n**(3)**\nby adding at the end the following:\n(f) Claim construction For the purposes of this chapter\u2014 (1) each challenged claim of a patent, and each substitute claim proposed in a motion to amend, shall be construed as the claim would be construed under section 282(b) in an action to invalidate a patent, including by construing each such claim in accordance with\u2014 (A) the ordinary and customary meaning of the claim as understood by a person having ordinary skill in the art to which the claimed invention pertains; and (B) the prosecution history pertaining to the patent; and (2) if a court has previously construed a challenged claim of a patent or a challenged claim term in a civil action to which the patent owner was a party, the Office shall consider that claim construction. .\n##### (f) Settlement\nSection 317(a) of title 35, United States Code, is amended by striking the second sentence.\n##### (g) Timing To issue trial certificate and decisions on rehearing\nSection 318 of title 35, United States Code, is amended\u2014\n**(1)**\nin subsection (b), by inserting , not later than 60 days after the date on which the parties to the inter partes review have informed the Director that the time for appeal has expired or any appeal has terminated, after the Director shall ; and\n**(2)**\nby adding at the end the following:\n(e) Rehearing Not later than 90 days after the date on which a request for rehearing of a final written decision issued by the Patent and Trial Appeal Board under subsection (a) is filed, the Board or the Director shall finally decide any request for reconsideration, rehearing, or review that is submitted with respect to the decision, except that the Director may, for good cause shown, extend that 90-day period by not more than 60 days. (f) Review by director (1) In general The Director may grant rehearing, reconsideration, or review of a decision by the Patent Trial and Appeal Board issued under this chapter. (2) Requirements Any reconsideration, rehearing, or review by the Director, as described in paragraph (1), shall be issued in a separate written opinion that\u2014 (A) is made part of the public record; and (B) sets forth the reasons for the reconsideration, rehearing, or review of the applicable decision by the Patent Trial and Appeal Board. (g) Rule of construction For the purposes of an appeal permitted under section 141, any decision on rehearing, reconsideration, or review of a final written decision of the Patent Trial and Appeal Board under subsection (a) of this section that is issued by the Director shall be deemed to be a final written decision of the Patent Trial and Appeal Board. .\n##### (h) Timing To issue decisions on remand\nSection 319 of title 35, United States Code, is amended\u2014\n**(1)**\nby striking A party and inserting the following:\n(a) In general A party ; and\n**(2)**\nby adding at the end the following:\n(b) Timing on remand after appeal Not later than 120 days after the date on which a mandate issues from the court remanding to the Patent Trial and Appeal Board after an appeal under subsection (a), the Board or the Director shall finally decide any issue on remand, except that the Director may, for good cause shown, extend that 120-day period by not more than 60 days. .\n#### 5. Post-grant review\n##### (a) Real parties in interest\nSection 321 of title 35, United States Code, is amended by adding at the end the following:\n(d) Real party in interest For purposes of this chapter, a person that, directly or through an affiliate, subsidiary, or proxy, makes a financial contribution to the preparation for, or conduct during, a post-grant review on behalf of a petitioner shall be considered a real party in interest of that petitioner. .\n##### (b) Timing To issue decisions on rehearing\nSection 324 of title 35, United States Code, is amended by adding at the end the following:\n(f) Rehearing Not later than 45 days after the date on which a request for rehearing from a determination by the Director under subsection (c) is filed, the Director shall finally decide any request for reconsideration, rehearing, or review with respect to the determination, except that the Director may, for good cause shown, extend that 45-day period by not more than 30 days. .\n##### (c) Eliminating repetitive proceedings\nSection 325 of title 35, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (c) through (f) as subsections (d) through (g), respectively;\n**(2)**\nby inserting after subsection (b) the following:\n(c) Single forum (1) In general If a post-grant review is instituted challenging the validity of a patent, the petitioner, a real party in interest, or a privy of the petitioner may not file or maintain, in a civil action arising in whole or in part under section 1338 of title 28, or in a proceeding before the International Trade Commission under section 337 of the Tariff Act of 1930 ( 19 U.S.C. 1337 ), a claim, a counterclaim, or an affirmative defense challenging the validity of any claim of the patent. (2) Considerations In determining whether to institute a proceeding under this chapter, subject to the provisions of subsections (a)(1) and (h), the Director may not reject a petition requesting a post-grant review on the basis of the petitioner, a real party in interest, or a privy of the petitioner filing or maintaining a claim, a counterclaim, or an affirmative defense challenging the validity of the patent in any civil action arising in whole or in part under section 1338 of title 28, or in a proceeding before the International Trade Commission under section 337 of the Tariff Act of 1930 ( 19 U.S.C. 1337 ). ;\n**(3)**\nby amending subsection (e), as so redesignated, to read as follows:\n(e) Multiple proceedings (1) In general Notwithstanding sections 135(a), 251, and 252, and chapter 30, after a petition to institute a post-grant review is filed, if another proceeding or matter involving the patent is before the Office\u2014 (A) the parties shall notify the Director of that other proceeding or matter\u2014 (i) not later than 30 days after the date of entry of the notice of filing date accorded to the petition; or (ii) if the other proceeding or matter is filed after the date on which the petition to institute an inter partes review is filed, not later than 30 days after the date on which the other proceeding or matter is filed; and (B) the Director shall issue a decision determining the manner in which the post-grant review or other proceeding or matter may proceed, including providing for stay, transfer, consolidation, or termination of any such matter or proceeding. (2) Considerations In determining whether to institute a proceeding under this chapter, the Director shall, unless the Director determines that the petitioner has demonstrated exceptional circumstances, reject any petition that presents prior art or an argument that is the same or substantially the same as prior art or an argument that previously was presented to the Office. ;\n**(4)**\nby amending subsection (f), as so redesignated, to read as follows:\n(f) Estoppel (1) In general A petitioner that has previously requested a post-grant review of a claim in a patent under this chapter, or a real party in interest or a privy of a petitioner, may not request or maintain another proceeding before the Office with respect to that patent on any ground that the petitioner raised or reasonably could have raised in the petition requesting or during the prior post-grant review, unless\u2014 (A) after the filing of the initial petition, the petitioner, or a real party in interest or a privy of the petitioner, is charged with infringement of additional claims of the patent; (B) a subsequent petition requests an inter partes review of only the additional claims of the patent that the petitioner, or a real party in interest or a privy of the petitioner, is later charged with infringing; and (C) that subsequent petition is accompanied by a request for joinder to the prior post-grant review, which the Director shall grant if the Director authorizes a post-grant review to be instituted on the subsequent petition under section 324. (2) Joined party Any person joined as a party to a post-grant review, and any real party in interest or any privy of such person, shall be estopped under this subsection and subsections (c)(1) and (e)(2) to the same extent as if that person, real party in interest, or privy had been the first petitioner in that post-grant review. ; and\n**(5)**\nby adding at the end the following:\n(h) Federal court and International Trade Commission validity determinations A post-grant review of a patent claim may not be instituted or maintained if, in a civil action arising in whole or in part under section 1338 of title 28, or in a proceeding before the International Trade Commission under section 337 of the Tariff Act of 1930 ( 19 U.S.C. 1337 ), in which the petitioner, a real party in interest, or a privy of the petitioner is a party, the court, or the International Trade Commission, as applicable, has entered a final judgment that decides a challenge to the validity of the patent claim. .\n##### (d) Conduct of post-Grant review\nSection 326 of title 35, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby amending paragraph (5) to read as follows:\n(5) setting forth standards and procedures for discovery of relevant evidence, including that such discovery shall be limited to\u2014 (A) the deposition of witnesses submitting affidavits or declarations; (B) evidence identifying the real parties in interest of the petitioner; and (C) what is otherwise necessary in the interest of justice; ;\n**(B)**\nby amending paragraph (9) to read as follows:\n(9) setting forth standards and procedures for\u2014 (A) allowing the patent owner to move to amend the patent under subsection (d) to cancel a challenged claim or propose a reasonable number of substitute claims; (B) allowing the Patent Trial and Appeal Board to provide guidance on substitute claims proposed by the patent owner; (C) allowing the patent owner to further revise proposed substitute claims after the issuance of guidance described in subparagraph (B); and (D) ensuring that any information submitted by the patent owner in support of any amendment entered under subsection (d), and any guidance issued by the Patent Trial and Appeal Board, is made available to the public as part of the prosecution history of the patent; ;\n**(C)**\nin paragraph (11)\u2014\n**(i)**\nby striking section 325(c) and inserting section 325(d) ; and\n**(ii)**\nby striking and at the end;\n**(D)**\nin paragraph (12), by striking the period at the end and inserting ; and ; and\n**(E)**\nby adding at the end the following:\n(13) setting forth the standards for demonstrating exceptional circumstances under section 325(e)(2). ;\n**(2)**\nby amending subsection (e) to read as follows:\n(e) Evidentiary standards (1) Presumption of validity The presumption of validity under section 282(a) shall apply to previously issued claims of a patent that is challenged in a post-grant review under this chapter. (2) Burden of proof In a post-grant review under this chapter\u2014 (A) the petitioner shall have the burden of proving a proposition of unpatentability of a previously issued claim of a patent by clear and convincing evidence; and (B) the petitioner shall have the burden of persuasion, by a preponderance of the evidence, with respect to a proposition of unpatentability for any substitute claim proposed by the patent owner. ; and\n**(3)**\nby adding at the end the following:\n(f) Claim construction For the purposes of this chapter\u2014 (1) each challenged claim of a patent, and each substitute claim proposed in a motion to amend, shall be construed as the claim would be construed under section 282(b) in an action to invalidate a patent, including by construing each such claim in accordance with\u2014 (A) the ordinary and customary meaning of the claim as understood by a person having ordinary skill in the art to which the claimed invention pertains; and (B) the prosecution history pertaining to the patent; and (2) if a court has previously construed a challenged claim of a patent or a challenged claim term in a civil action to which the patent owner was a party, the Office shall consider that claim construction. .\n##### (e) Settlement\nSection 327(a) of title 35, United States Code, is amended by striking the second sentence.\n##### (f) Timing To issue trial certificates and decisions on rehearing\nSection 328 of title 35, United States Code, is amended\u2014\n**(1)**\nin subsection (b), by inserting , not later than 60 days after the date on which the parties to the post-grant review have informed the Director that the time for appeal has expired or any appeal has terminated, after the Director shall ; and\n**(2)**\nby adding at the end the following:\n(e) Rehearing Not later than 90 days after the date on which a request for rehearing of a final written decision issued by the Patent and Trial Appeal Board under subsection (a) is filed, the Board or the Director shall finally decide any request for reconsideration, rehearing, or review that is submitted with respect to the decision, except that the Director may, for good cause shown, extend that 90-day period by not more than 60 days. (f) Review by director (1) In general The Director may grant rehearing, reconsideration, or review of a decision by the Patent Trial and Appeal Board issued under this chapter. (2) Requirements Any reconsideration, rehearing, or review by the Director, as described in paragraph (1), shall be issued in a separate written opinion that\u2014 (A) is made part of the public record; and (B) sets forth the reasons for the reconsideration, rehearing, or review of the decision by the Patent Trial and Appeal Board. (g) Rule of construction For the purposes of an appeal permitted under section 141, any decision on rehearing, reconsideration, or review of a final written decision of the Patent Trial and Appeal Board under subsection (a) of this section that is issued by the Director shall be deemed to be a final written decision of the Patent Trial and Appeal Board. .\n##### (g) Timing To issue decisions on remand\nSection 329 of title 35, United States Code, is amended\u2014\n**(1)**\nby striking A party and inserting the following:\n(a) In general A party ; and\n**(2)**\nby adding at the end the following:\n(b) Timing on remand after appeal Not later than 120 days after the date on which a mandate issues from the court remanding to the Patent Trial and Appeal Board after an appeal under subsection (a), the Board or the Director shall finally decide any issue on remand, except that the Director may, for good cause shown, extend that 120-day period by not more than 60 days. .\n#### 6. Reexamination of patents\n##### (a) Request for reexamination\nSection 302 of title 35, United States Code, is amended by inserting after the second sentence the following: The request must identify all real parties in interest and certify that reexamination is not barred under section 303(d). .\n##### (b) Reexamination barred\nSection 303 of title 35, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking the third sentence; and\n**(2)**\nby adding at the end the following:\n(d) An ex parte reexamination may not be ordered if the request for reexamination is filed more than 1 year after the date on which the requester or a real party in interest or a privy of the requester is served with a complaint alleging infringement of the patent. For purposes of this chapter, a person that directly or through an affiliate, subsidiary, or proxy makes a financial contribution to the preparation for, or conduct during, an ex parte reexamination on behalf of a requester shall be considered a real party in interest of the requester. (e) In determining whether to order an ex parte reexamination, the Director\u2014 (1) shall, unless the Director determines that the requestor has demonstrated exceptional circumstances, reject any request that presents prior art or an argument that is the same or substantially the same as prior art or an argument that previously was presented to the Office; and (2) may reject any request that the Director determines has used a prior Office decision as a guide to correct or bolster a previous deficient request filed under this chapter or a previous deficient petition filed under chapter 31 or 32. .\n##### (c) Reexamination order by Director\nSection 304 of title 35, United States Code, is amended, in the first sentence, by inserting after resolution of the question the following: , unless the Director determines that the request for reexamination should be rejected under subsection (d) or (e) of section 303, in which case the Director shall issue an order denying reexamination .\n#### 7. Elimination of USPTO fee diversion\n##### (a) Funding\nSection 42 of title 35, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking All fees and inserting the following:\n(a) Fees for service by PTO All fees ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking All fees paid to the Director and all appropriations and inserting the following:\n(b) Innovation Promotion Fund All fees paid to the Director ; and\n**(B)**\nby striking Patent and Trademark Office Appropriation Account and inserting United States Patent and Trademark Office Innovation Promotion Fund ;\n**(3)**\nby striking subsection (c) and inserting the following:\n(c) Collection of funds for PTO activities (1) In general Fees authorized in this title or any other Act to be charged or established by the Director shall be collected by the Director and shall be available to the Director until expended to carry out the activities of the Patent and Trademark Office. (2) Use of fees (A) Patent fees Any fees that are collected under this title, and any surcharges on such fees, may only be used for expenses of the Office relating to the processing of patent applications and for other activities, services, and materials relating to patents and to cover a proportionate share of the administrative costs of the Office. (B) Trademark fees Any fees that are collected under section 31 of the Trademark Act of 1946 (as defined in subsection (d)(1)) ( 15 U.S.C. 1113 ), and any surcharges on such fees, may only be used for expenses of the Office relating to the processing of trademark registrations and for other activities, services, and materials relating to trademarks and to cover a proportionate share of the administrative costs of the Office. ;\n**(4)**\nby redesignating subsections (d) and (e) as subsections (e) and (f), respectively;\n**(5)**\nby inserting after subsection (c) the following:\n(d) Revolving fund (1) Definitions In this subsection\u2014 (A) the term Fund means the United States Patent and Trademark Office Innovation Promotion Fund established under paragraph (2); and (B) the term Trademark Act of 1946 means the Act entitled An Act to provide for the registration and protection of trademarks used in commerce, to carry out the provisions of certain international conventions, and for other purposes , approved July 5, 1946 ( 15 U.S.C. 1051 et seq. ), (commonly referred to as the Trademark Act of 1946 or the Lanham Act ). (2) Establishment There is established in the Treasury a revolving fund to be known as the United States Patent and Trademark Office Innovation Promotion Fund . (3) Derivation of resources There shall be deposited into the Fund any fees collected under\u2014 (A) this title; or (B) the Trademark Act of 1946. (4) Expenses Amounts deposited into the Fund under paragraph (3) shall be available, without fiscal year limitation, to cover\u2014 (A) to the extent consistent with the limitation on the use of fees under subsection (c), all expenses, including all administrative and operating expenses, determined by the Director to be ordinary and reasonable, incurred by the Director for the continued operation of all services, programs, activities, and duties of the Office relating to patents and trademarks, as such services, programs, activities, and duties are described under\u2014 (i) this title; and (ii) the Trademark Act of 1946; and (B) all expenses incurred pursuant to any obligation, representation, or other commitment of the Office. ;\n**(6)**\nin subsection (e), as so redesignated, by striking The Director and inserting the following:\n(e) Refunds The Director ; and\n**(7)**\nin subsection (f), as so redesignated, by striking The Secretary and inserting the following:\n(f) Report The Secretary .\n##### (b) Effective date; transfer from and termination of obsolete funds\n**(1) Effective date**\nThe amendments made by subsection (a) shall take effect on the first day of the first fiscal year that begins on or after the date of enactment of this Act.\n**(2) Remaining balances**\nOn the effective date described in paragraph (1), there shall be deposited in the United States Patent and Trademark Office Innovation Promotion Fund established under section 42(d)(2) of title 35, United States Code (as added by subsection (a)), any available unobligated balances remaining in the Patent and Trademark Office Appropriation Account, and in the Patent and Trademark Fee Reserve Fund established under section 42(c)(2) of title 35, United States Code, as in effect on the day before that effective date.\n**(3) Termination of reserve fund**\nUpon the payment of all obligated amounts in the Patent and Trademark Fee Reserve Fund under paragraph (2), the Patent and Trademark Fee Reserve Fund shall be terminated.\n#### 8. Institutions of higher education\nSection 123(d) of title 35, United States Code, is amended to read as follows:\n(d) Institutions of higher education (1) Definition In this subsection, the term institution of higher education has the meaning given the term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ). (2) Inclusions For purposes of this section, a micro entity shall include an applicant who certifies that\u2014 (A) the applicant\u2019s employer, from which the applicant obtains the majority of the applicant\u2019s income, is an institution of higher education; (B) the applicant has assigned, granted, conveyed, or is under an obligation by contract or law to assign, grant, or convey, a license or other ownership interest in the particular applications to an institution of higher education; (C) the applicant is an institution of higher education; or (D) the applicant is an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code that holds title to patents and patent applications on behalf of an institution of higher education for the purpose of facilitating commercialization of the technologies of the patents and patent applications. .\n#### 9. Assisting small businesses in the United States patent system\n##### (a) Definition\nIn this section, the term small business concern has the meaning given the term in section 3 of the Small Business Act ( 15 U.S.C. 632 ).\n##### (b) Small business administration report\nNot later than 1 year after the date of the enactment of this Act, the Administrator of the Small Business Administration, using existing resources, shall submit to the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives a report analyzing the impact of\u2014\n**(1)**\npatent ownership by small business concerns; and\n**(2)**\ncivil actions against small business concerns arising under title 35, United States Code, relating to patent infringement.\n##### (c) Free online availability of public search facility materials\nSection 41(i) of title 35, United States Code, is amended by adding at the end the following:\n(5) Free online availability of public search facility materials The Director shall make available online and at no charge all patent and trademark information that is available at the Public Search Facility of the Office located in Alexandria, Virginia, including, except to the extent that licenses with third-party contractors would make such provision financially unviable\u2014 (A) search tools and databases; (B) informational materials; and (C) training classes and materials. .",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-01",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1553",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PREVAIL Act",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-20T14:49:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr3160",
          "measure-number": "3160",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-01",
          "originChamber": "HOUSE",
          "update-date": "2026-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3160v00",
            "update-date": "2026-02-03"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Promoting and Respecting Economically Vital American Innovation Leadership Act or the PREVAIL Act</strong></p><p>This bill addresses various issues relating to the U.S. Patent and Trademark Office (USPTO), including by imposing additional requirements on administrative patent validity challenges (proceedings to review and potentially cancel issued patents) at the USPTO.</p><p>The bill modifies provisions relating to inter partes reviews (IPRs) and other administrative patent validity proceedings, including by</p><ul><li>prohibiting an administrative patent judge who participated in deciding whether to institute an IPR (i.e., whether to allow the IPR to proceed based on the initial petition) from also participating in deciding the final outcome of the same IPR;</li><li>prohibiting a person (individual or entity) from petitioning for an IPR against a patent unless the person meets certain standing requirements (currently, any person may petition for an IPR);</li><li>prohibiting a person who has challenged a patent's validity in an IPR from raising the same challenges against the patent in other proceedings (e.g., district court) if the IPR has been instituted; and</li><li>raising the burden that the petitioner in an IPR must meet to invalidate a previously\u00a0issued patent claim.</li></ul><p>The bill also makes institutions of higher education (IHEs) and nonprofit entities that hold patents on behalf of IHEs eligible for reduced patent-related fees, including filing fees. (Currently, employees of IHEs are eligible for reduced fees but not the IHEs themselves.)</p><p>The bill also makes fees collected by the USPTO available for the USPTO's use without further appropriations from Congress.</p>"
        },
        "title": "PREVAIL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3160.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Promoting and Respecting Economically Vital American Innovation Leadership Act or the PREVAIL Act</strong></p><p>This bill addresses various issues relating to the U.S. Patent and Trademark Office (USPTO), including by imposing additional requirements on administrative patent validity challenges (proceedings to review and potentially cancel issued patents) at the USPTO.</p><p>The bill modifies provisions relating to inter partes reviews (IPRs) and other administrative patent validity proceedings, including by</p><ul><li>prohibiting an administrative patent judge who participated in deciding whether to institute an IPR (i.e., whether to allow the IPR to proceed based on the initial petition) from also participating in deciding the final outcome of the same IPR;</li><li>prohibiting a person (individual or entity) from petitioning for an IPR against a patent unless the person meets certain standing requirements (currently, any person may petition for an IPR);</li><li>prohibiting a person who has challenged a patent's validity in an IPR from raising the same challenges against the patent in other proceedings (e.g., district court) if the IPR has been instituted; and</li><li>raising the burden that the petitioner in an IPR must meet to invalidate a previously\u00a0issued patent claim.</li></ul><p>The bill also makes institutions of higher education (IHEs) and nonprofit entities that hold patents on behalf of IHEs eligible for reduced patent-related fees, including filing fees. (Currently, employees of IHEs are eligible for reduced fees but not the IHEs themselves.)</p><p>The bill also makes fees collected by the USPTO available for the USPTO's use without further appropriations from Congress.</p>",
      "updateDate": "2026-02-03",
      "versionCode": "id119hr3160"
    },
    "title": "PREVAIL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Promoting and Respecting Economically Vital American Innovation Leadership Act or the PREVAIL Act</strong></p><p>This bill addresses various issues relating to the U.S. Patent and Trademark Office (USPTO), including by imposing additional requirements on administrative patent validity challenges (proceedings to review and potentially cancel issued patents) at the USPTO.</p><p>The bill modifies provisions relating to inter partes reviews (IPRs) and other administrative patent validity proceedings, including by</p><ul><li>prohibiting an administrative patent judge who participated in deciding whether to institute an IPR (i.e., whether to allow the IPR to proceed based on the initial petition) from also participating in deciding the final outcome of the same IPR;</li><li>prohibiting a person (individual or entity) from petitioning for an IPR against a patent unless the person meets certain standing requirements (currently, any person may petition for an IPR);</li><li>prohibiting a person who has challenged a patent's validity in an IPR from raising the same challenges against the patent in other proceedings (e.g., district court) if the IPR has been instituted; and</li><li>raising the burden that the petitioner in an IPR must meet to invalidate a previously\u00a0issued patent claim.</li></ul><p>The bill also makes institutions of higher education (IHEs) and nonprofit entities that hold patents on behalf of IHEs eligible for reduced patent-related fees, including filing fees. (Currently, employees of IHEs are eligible for reduced fees but not the IHEs themselves.)</p><p>The bill also makes fees collected by the USPTO available for the USPTO's use without further appropriations from Congress.</p>",
      "updateDate": "2026-02-03",
      "versionCode": "id119hr3160"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3160ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "PREVAIL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PREVAIL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting and Respecting Economically Vital American Innovation Leadership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 35, United States Code, to invest in inventors in the United States, maintain the United States as the leading innovation economy in the world, and protect the property rights of the inventors that grow the economy of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:25Z"
    }
  ]
}
```
