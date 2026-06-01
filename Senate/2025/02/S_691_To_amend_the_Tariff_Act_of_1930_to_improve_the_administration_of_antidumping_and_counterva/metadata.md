# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/691?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/691
- Title: Leveling the Playing Field 2.0 Act
- Congress: 119
- Bill type: S
- Bill number: 691
- Origin chamber: Senate
- Introduced date: 2025-02-24
- Update date: 2026-05-11T16:34:50Z
- Update date including text: 2026-05-11T16:34:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in Senate
- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-24: Introduced in Senate

## Actions

- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/691",
    "number": "691",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Leveling the Playing Field 2.0 Act",
    "type": "S",
    "updateDate": "2026-05-11T16:34:50Z",
    "updateDateIncludingText": "2026-05-11T16:34:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-02-24T21:24:25Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-24T21:24:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MN"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "AL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MN"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "SC"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "WI"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "AR"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "PA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "MS"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "AZ"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "IN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MA"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "MO"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "AL"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-16",
      "state": "WV"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "MS"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NH"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "WV"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-05",
      "state": "PA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s691is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 691\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2025 Ms. Smith (for Mr. Young (for himself, Ms. Smith , Mr. Tuberville , Ms. Klobuchar , Mr. Graham , Ms. Baldwin , Mr. Cotton , Mr. Fetterman , Mr. Wicker , Mr. Gallego , Mr. Banks , Ms. Warren , Mr. Schmitt , Mrs. Gillibrand , and Mr. Moreno )) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Tariff Act of 1930 to improve the administration of antidumping and countervailing duty laws, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Leveling the Playing Field 2.0 Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Successive investigations\nSec. 101. Establishment of special rules for determination of material injury in the case of successive antidumping and countervailing duty investigations.\nSec. 102. Initiation of successive antidumping and countervailing duty investigations.\nSec. 103. Issuance of determinations with respect to successive antidumping and countervailing duty investigations.\nTITLE II\u2014Responding to market distortions\nSec. 201. Addressing cross-border subsidies in countervailing duty investigations.\nSec. 202. Modification of definition of ordinary course of trade to specify that an insufficient quantity of foreign like products constitutes a situation outside the ordinary course of trade.\nSec. 203. Modification of adjustments to export price and constructed export price with respect to duty drawback.\nSec. 204. Modification of determination of normal value to account for distortions of costs that occur in foreign countries.\nSec. 205. Special rules for calculation of cost of production and constructed value to address distorted costs.\nTITLE III\u2014Preventing circumvention\nSec. 301. Modification of requirements in circumvention inquiries.\nSec. 302. Requirement of provision by importer of certification by importer or other party.\nSec. 303. Clarification of authority for Department of Commerce regarding merchandise covered by antidumping and countervailing duty proceedings.\nSec. 304. Asset requirements applicable to nonresident importers.\nTITLE IV\u2014Countering currency undervaluation\nSec. 401. Investigation or review of currency undervaluation under countervailing duty law.\nSec. 402. Determination of benefit with respect to currency undervaluation.\nTITLE V\u2014Preventing duty evasion\nSec. 501. Limitation on protest against decisions of U.S. Customs and Border Protection of claims of evasion of antidumping and countervailing duty orders.\nSec. 502. Procedures for investigating claims of evasion of safeguard actions.\nSec. 503. Application of provisions relating to certain proprietary information.\nTITLE VI\u2014General provisions\nSec. 601. Application to Canada and Mexico.\nSec. 602. Effective date.\nI\nSuccessive investigations\n#### 101. Establishment of special rules for determination of material injury in the case of successive antidumping and countervailing duty investigations\n##### (a) In general\nSection 771(7) of the Tariff Act of 1930 ( 19 U.S.C. 1677(7) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (E) through (J) as subparagraphs (F) through (K), respectively;\n**(2)**\nin subparagraph (I), as redesignated by paragraph (1)\u2014\n**(A)**\nby striking subparagraph (G)(ii) and inserting subparagraph (H)(ii) ; and\n**(B)**\nby striking subparagraph (F) and inserting subparagraph (G) ; and\n**(3)**\nby inserting after subparagraph (D) the following:\n(E) Special rules for successive investigations (i) In general (I) Evaluation of impact on domestic industry In evaluating the impact of imports of the merchandise on producers of domestic like products under subparagraph (C)(iii), the Commission shall\u2014 (aa) consider the condition of the domestic industry as found in a recently completed investigation; (bb) consider the effect of a concurrent investigation or recently completed investigation on trade and the financial performance of the domestic industry, including whether the imports are likely to lead to the continuation or recurrence of material injury determined by the Commission in any concurrent investigation or recently completed investigation; and (cc) include in the record any prior injury determinations by the Commission with respect to imports of the merchandise. (II) Effect of recent improvement on material injury determination For the purposes of this subparagraph, the Commission may not find that there is no material injury or threat of material injury to a domestic industry solely based on recent improvements in the industry\u2019s performance, such as an increase in sales, market share, or profitability of domestic producers, that are related to relief granted pursuant to a concurrent investigation or recently completed investigation. (ii) Retroactive application of final determination In making any finding under section 705(b)(4)(A) or 735(b)(4)(A) in a successive investigation, the Commission shall consider that a concurrent investigation or recently completed investigation contributes to the likelihood that the remedial effect of the countervailing duty order to be issued under section 706 or the antidumping duty order to be issued under section 736 will be seriously undermined. .\n##### (b) Definitions\nSection 771 of the Tariff Act of 1930 ( 19 U.S.C. 1677 ) is amended by adding at the end the following:\n(37) Treatment of successive investigations For purposes of paragraph (7)(E) and sections 702(f), 732(f), and 784: (A) Concurrent investigation The term concurrent investigation means an ongoing investigation in which an affirmative determination under section 703(a) or 733(a) has been made by the Commission with respect to imports of a class or kind of merchandise that are the same or similar to imports of a class or kind of merchandise that are the subject of a successive investigation. (B) Recently completed investigation The term recently completed investigation means a completed investigation in which an affirmative determination under section 705(b) or 735(b) was issued by the Commission with respect to imports of a class or kind of merchandise that are the same or similar to imports of a class or kind of merchandise that are the subject of a successive investigation not more than 2 years before the date of initiation of the successive investigation. (C) Successive investigation The term successive investigation means an investigation that has been initiated by the administering authority following a petition filed pursuant to section 702(f) or 732(f). .\n#### 102. Initiation of successive antidumping and countervailing duty investigations\n##### (a) Countervailing duty investigation\nSection 702 of the Tariff Act of 1930 ( 19 U.S.C. 1671a ) is amended by adding at the end the following:\n(f) Initiation by administering authority of successive countervailing duty investigation A successive investigation shall be initiated\u2014 (1) under subsection (a), if\u2014 (A) the requirements under that subsection are met with respect to imports of a class or kind of merchandise; and (B) imports of the same or similar class or kind of merchandise are or have been the subject of a concurrent investigation or recently completed investigation; or (2) under subsection (b), if\u2014 (A) the determinations under clauses (i) and (ii) of subsection (c)(1)(A) are affirmative with respect to imports of a class or kind of merchandise; and (B) imports of the same or similar class or kind of merchandise are or have been the subject of a concurrent investigation or recently completed investigation. .\n##### (b) Antidumping duty investigation\nSection 732 of the Tariff Act of 1930 ( 19 U.S.C. 1673a ) is amended by adding at the end the following:\n(f) Initiation by administering authority of successive antidumping duty investigation A successive investigation shall be initiated\u2014 (1) under subsection (a), if\u2014 (A) the requirements under that subsection are met with respect to imports of a class or kind of merchandise; and (B) imports of the same or similar class or kind of merchandise are or have been the subject of a concurrent investigation or recently completed investigation; or (2) under subsection (b), if\u2014 (A) the determinations under clauses (i) and (ii) of subsection (c)(1)(A) are affirmative with respect to imports of a class or kind of merchandise; and (B) imports of the same or similar class or kind of merchandise are or have been the subject of a concurrent investigation or recently completed investigation. .\n#### 103. Issuance of determinations with respect to successive antidumping and countervailing duty investigations\n##### (a) In general\nSubtitle D of title VII of the Tariff Act of 1930 ( 19 U.S.C. 1677 et seq. ) is amended by adding at the end the following:\n784. Determinations relating to successive investigations (a) In general Notwithstanding any other provision of this title, the administering authority\u2014 (1) with respect to a successive investigation under section 702(f)\u2014 (A) shall issue a preliminary determination under section 703(b) not later than 85 days after initiating the investigation; (B) may not postpone under section 703(c) such deadline for the issuance of a preliminary determination unless requested by the petitioner; (C) upon receipt of an allegation by the petitioner pursuant to section 703(e), shall make a determination under section 703(e) with respect to the investigation; (D) shall issue a final determination under section 705(a) not later than 75 days after issuing the preliminary determination under subparagraph (A); and (E) shall extend the date of the final determination under section 705(a) if requested by the petitioner; and (2) with respect to a successive investigation under section 732(f)\u2014 (A) shall issue a preliminary determination under section 733(b) not later than 140 days after initiating the investigation; (B) may not postpone under section 733(c) such deadline for the issuance of a preliminary determination unless requested by the petitioner; (C) upon receipt of an allegation by the petitioner pursuant to section 733(e), shall make a determination under section 733(e) with respect to the investigation; (D) shall issue a final determination under section 735(a) not later than 75 days after issuing the preliminary determination under subparagraph (A); and (E) may extend the date of the final determination under section 735(a)(2) if requested by the petitioner. .\n##### (b) Clerical amendment\nThe table of contents for the Tariff Act of 1930 is amended by inserting after the item relating to section 783 the following:\nSec. 784. Determinations relating to successive investigations. .\nII\nResponding to market distortions\n#### 201. Addressing cross-border subsidies in countervailing duty investigations\n##### (a) In general\nSection 701(d) of the Tariff Act of 1930 ( 19 U.S.C. 1671(d) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking Treatment of international consortia and inserting Cumulation of cross-Border subsidies ;\n**(2)**\nby striking For purposes and inserting the following:\n(1) International consortia and multinational corporations For purposes ;\n**(3)**\nin paragraph (1), as designated by paragraph (2)\u2014\n**(A)**\nby inserting after in their respective home countries, the following: or multinational corporations that are engaged in the production of subject merchandise receive countervailable subsidies to assist, permit, or otherwise enable their production or manufacturing operations in the country in which the class or kind of merchandise is produced, exported, or sold (or likely to be sold) for importation into the United States, ; and\n**(B)**\nby inserting after the international consortium the following: or multinational corporation ; and\n**(4)**\nby adding at the end the following:\n(2) Transnational subsidies (A) In general For purposes of this subtitle, if there is a countervailable subsidy by a government of a third country or any public entity within the territory of a third country with respect to the manufacture, production, or export of a class or kind of merchandise that is produced, exported, or sold (or likely to be sold) for importation into the United States from the territory of the subject country, and the government of the subject country or any public entity within the territory of the subject country facilitates the provision of such subsidy, then the administering authority shall treat the subsidy as having been provided by the government of the subject country or a public entity within the territory of the subject country and shall cumulate all such countervailable subsidies, as well as countervailable subsidies provided directly or indirectly by the government or any public entity within the territory of the subject country. (B) Application This paragraph shall be applied in a manner consistent with the international obligations of the United States. .\n##### (b) Definitions\nSection 771 of the Tariff Act of 1930 ( 19 U.S.C. 1677 ) is amended\u2014\n**(1)**\nin paragraph (5A), by inserting after subparagraph (D) the following:\n(E) Transnational subsidy In determining whether a transnational subsidy is a specific subsidy, in law or in fact, the administering authority shall examine the situation in the subject country based on subparagraphs (B), (C), and (D). ;\n**(2)**\nin paragraph (9)\u2014\n**(A)**\nin subparagraph (F), by striking and at the end;\n**(B)**\nin subparagraph (G), by striking the period at the end and inserting , and ; and\n**(C)**\nby adding at the end the following:\n(H) in any proceeding under subtitle A involving a transnational subsidy, the government of the third country. ; and\n**(3)**\nby adding at the end the following:\n(38) Multinational corporation The term multinational corporation means a person, firm, or corporation that owns or controls, directly or indirectly, facilities for the production of subject merchandise in two or more foreign countries. .\n##### (c) Upstream subsidies\nSection 771A of the Tariff Act of 1930 ( 19 U.S.C. 1677\u20131 ) is amended by adding at the end the following:\n(d) Multinational corporations (1) In general This section shall apply to purchases of input products by multinational corporations if\u2014 (A) the multinational corporation manufactures or produces merchandise in a country that is the subject of a countervailing duty proceeding; (B) the multinational corporation purchases the input product from a cross-owned company located in a third country with respect to which the administering authority has made an affirmative determination under section 703(b)(1) or 705(a)(1) with respect to a countervailable subsidy provided\u2014 (i) for the manufacture, production, or exportation of that input product; or (ii) to that cross-owned company; and (C) in the judgment of the administering authority, the countervailing subsidy described in subparagraph (B) bestows a competitive benefit on that merchandise. (2) Timing of subsidy If a countervailable subsidy is provided to a multinational corporation or a cross-owned company that did not exist at the time the administering authority made an affirmative determination described in paragraph (1)(B), the administering authority is not precluded from examining the subsidy under paragraph (1). (3) Application This subsection shall be applied in a manner consistent with the international obligations of the United States. (4) Definitions In this subsection: (A) Cross-owned company; multinational corporation The terms cross-owned company and multinational corporation have the meanings given those terms as defined by the administering authority by regulation. (B) Upstream subsidy The term upstream subsidy has the meaning given that term in subsection (a), except that the term shall include an export subsidy. .\n#### 202. Modification of definition of ordinary course of trade to specify that an insufficient quantity of foreign like products constitutes a situation outside the ordinary course of trade\nSection 771(15) of the Tariff Act of 1930 ( 19 U.S.C. 1677(15) ) is amended by adding at the end the following:\n(D) Situations in which the quantity of a foreign like product selected for comparison under section 771(16) is insufficient to establish a proper comparison to the export price or constructed export price. .\n#### 203. Modification of adjustments to export price and constructed export price with respect to duty drawback\nSection 772(c)(1)(B) of the Tariff Act of 1930 ( 19 U.S.C. 1677a(c)(1)(B) ) is amended\u2014\n**(1)**\nby striking any ; and\n**(2)**\nby inserting after United States the following: , but that amount shall not exceed the per unit amount of such duties contained in the weighted average cost of production .\n#### 204. Modification of determination of normal value to account for distortions of costs that occur in foreign countries\n##### (a) Normal value\n**(1) In general**\nSection 773(b)(3) of the Tariff Act of 1930 ( 19 U.S.C. 1677b(b)(3) ) is amended\u2014\n**(A)**\nin subparagraph (A), by striking business and inserting trade ; and\n**(B)**\nin the flush text after subparagraph (C), by inserting before For purposes the following: For purposes of subparagraph (A), if a particular market situation exists such that the cost of materials and fabrication or other processing of any kind does not reasonably reflect the cost of production in the ordinary course of trade, the administering authority may use another calculation methodology under this subtitle or any other calculation methodology. .\n**(2) Reflection of costs of production**\nSection 773(e) of the Tariff Act of 1930 ( 19 U.S.C. 1677b(e) ) is amended, in the first sentence of the flush text after paragraph (3), by striking accurately and inserting reasonably .\n##### (b) Modification of definition of ordinary course of trade\nSection 771(15) of the Tariff Act of 1930 ( 19 U.S.C. 1677(15)(C) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) through (C) as clauses (i) through (iii), respectively, and moving those clauses, as so redesignating, two ems to the right;\n**(2)**\nby striking The term and inserting the following:\n(A) In general The term ;\n**(3)**\nin subparagraph (A), as designated by paragraph (2), in clause (iii), as redesignated by paragraph (1)\u2014\n**(A)**\nby striking that the particular market situation prevents and inserting \u201cthat a particular market situation exists that\u2014\n(I) prevents ;\n**(B)**\nin subclause (I), as designated by subparagraph (A), by striking the period at the end and inserting , relating to normal value determined under subsection (a) of section 773; or ; and\n**(C)**\nby adding at the end the following:\n(II) distorts costs of production, relating to normal value determined under subsections (b) and (e) of section 773. ; and\n**(4)**\nby adding at the end the following:\n(B) Cost of production For purposes of making a determination under subparagraph (A)(iii)(II) with respect to subject merchandise, the administering authority shall determine that a particular market situation exists that distorts costs of production if a particular market situation exists such that the cost of materials and fabrication or other processing of any kind does not reasonably reflect the cost of production in the ordinary course of trade. .\n##### (c) Definition of particular market situation\nSection 771 of the Tariff Act of 1930 ( 19 U.S.C. 1677 ), as amended by sections 101(b) and 201(b)(3), is further amended by adding at the end the following:\n(39) Particular market situation (A) In general The term particular market situation means a certain circumstance or set of circumstances that the administering authority determines either prevents a proper comparison of prices in the comparison market with the export price or constructed export price or distorts the costs of production of the subject merchandise. (B) Distortion of costs of production (i) Examples of distortions of costs of production that may create a particular market situation Examples of circumstances that are likely to distort the costs of production and thus are deemed to create a particular market situation for subject merchandise for purposes of subparagraph (A) include the following circumstances: (I) An input into the production of subject merchandise is produced in such amounts that there is more supply than demand in international markets for the input. (II) A foreign government, a state-owned enterprise, or any other public body is the predominant producer or supplier of an input into the production of subject merchandise. (III) A foreign government intervenes in the market for an input into the production of subject merchandise. (IV) A foreign government limits exports of an input into the production of subject merchandise. (V) A foreign government imposes export taxes on an input into the production of subject merchandise. (VI) A foreign government exempts an importer, producer, or exporter of subject merchandise from paying duties or taxes associated with trade remedies established by the foreign government relating to an input into the production of subject merchandise. (VII) A foreign government rebates duties or taxes paid by an importer, producer, or exporter of subject merchandise associated with trade remedies established by the foreign government related to an input into the production of subject merchandise. (VIII) A foreign government provides financial assistance or support to the producer or exporter of subject merchandise, or to a producer or supplier of an input into the production of subject merchandise. (IX) A foreign government takes action that influences the production of subject merchandise or an input into the production of subject merchandise, such as domestic content and technology transfer requirements. (X) A foreign government does not enforce its property (including intellectual property), human rights, labor, or environmental protection laws and policies, or those laws and policies are otherwise shown to be ineffective with respect to either a producer or exporter of subject merchandise, or to a producer or supplier of an input into the production of subject merchandise in the subject country. (XI) A foreign government does not implement property (including intellectual property), human rights, labor, or environmental protection laws and policies. (XII) A business relationship between one or more producers of subject merchandise and suppliers of inputs to the production of subject merchandise is such that prices of the inputs are not determined in accordance with general market principles, such as through a strategic alliance or noncompetitive arrangement. (ii) Distortions caused by particular market situations need not be quantified If the administering authority determines the existence of a particular market situation under subparagraph (A) but cannot measure the distortions caused by that particular market situation on prices or costs in the exporting country, the administering authority is not required to quantify those distortions and may use any available information and methodology to address those distortions in its analysis and calculations. (iii) Particular market situations may exist in multiple countries (I) In general The same market situation, or a similar market situation, that distorts the costs of production of the subject merchandise can exist in multiple countries or markets and still be considered particular if the administering authority determines that a market situation exists that distorts costs of production for certain products or parties in the subject country. (II) No limitation There is no limitation to the number of products or parties that may be impacted by a particular market situation. (C) Other factors In finding that a particular market situation exists, or in using another calculation methodology under this paragraph, the administering authority is not required to consider\u2014 (i) the costs or prices that would otherwise exist in the ordinary course of trade in the absence of the particular market situation or any of its contributing circumstances; (ii) whether there is any difference between the particular market situation or any of its contributing circumstances in the exporting country as opposed to any other country; or (iii) the length of time that the particular market situation or any of its contributing circumstances has existed. .\n#### 205. Special rules for calculation of cost of production and constructed value to address distorted costs\nSection 773(f)(3) of the Tariff Act of 1930 ( 19 U.S.C. 1677b(f)(3) ) is amended\u2014\n**(1)**\nby striking If, in the case and inserting the following:\n(A) Major inputs from affiliated persons If, in the case ; and\n**(2)**\nby adding at the end the following:\n(B) Major inputs from certain unaffiliated persons (i) In general In the case of a transaction between the exporter or producer of the merchandise and any unaffiliated person described in clause (ii) involving a major input to the merchandise, the administering authority may value such major input based on the information available regarding what the amount would have been if the transaction had occurred between the exporter or producer of the merchandise and an unaffiliated person that is not described in clause (ii) if that amount is greater than the amount reflected in the records of the exporter or producer of the merchandise. (ii) Unaffiliated persons described An unaffiliated person described in this clause is\u2014 (I) any person in a nonmarket economy country; (II) any producer, exporter, or supplier of the input described in clause (i) found by the administering authority, or by any investigating authority of a third country, to be receiving a countervailable subsidy pertaining to an identical or comparable input in the subject country if there is no countervailing duty imposed on the input pursuant to a measure in effect in the exporting country based upon a finding by the investigating authority of the exporting country that the producer or supplier of the input described in clause (i) received a countervailable subsidy; (III) any producer, exporter, or supplier of the input described in clause (i) found by the administering authority, or by any investigating authority of a third country to be selling an identical or comparable input for less than fair market value in the subject country if there is no antidumping duty imposed on the input pursuant to a measure in effect in the exporting country based upon a finding by the investigating authority of the exporting country that the producer or supplier sold the input described in clause (i) for less than fair market value into the subject country; (IV) a government or public body within the territory of the exporting country or any other country; or (V) a group of governments or public bodies, or a combination thereof, that collectively account for a meaningful share of the production of the input described in clause (i). (iii) Application Subclauses (I), (II), and (III) of clause (ii) shall not apply to inputs described in clause (i) that are produced in the exporting country. .\nIII\nPreventing circumvention\n#### 301. Modification of requirements in circumvention inquiries\n##### (a) In general\nSection 781 of the Tariff Act of 1930 ( 19 U.S.C. 1677j ) is amended by striking subsection (f) and inserting the following:\n(f) Procedures for conducting circumvention inquiries (1) Initiation by administering authority A circumvention inquiry shall be initiated whenever the administering authority determines, from information available to it, that a formal inquiry is warranted into the question of whether the elements necessary for a determination under this section exist. (2) Initiation by inquiry request (A) In general A circumvention inquiry shall be initiated whenever an interested party files an inquiry request that alleges the elements necessary for a determination under this section, accompanied by information reasonably available to the requestor supporting those allegations. (B) Rules The administering authority shall specify requirements for the contents and service of an inquiry request under subparagraph (A). (C) Acceptance of communications The administering authority shall not accept any unsolicited oral or written communication from any person other than the interested party filing an inquiry request before the administering authority decides whether to initiate an inquiry, except for communications regarding the status of the consideration of the inquiry request. (3) Action with respect to inquiry request (A) In general Subject to subparagraph (B), not later than 45 days after the filing of an inquiry request under paragraph (2)(A), the administering authority shall\u2014 (i) initiate a circumvention inquiry; (ii) dismiss the inquiry request as inadequate and notify the requestor in writing of the reasons for the dismissal; or (iii) notify all interested parties that the inquiry request will be addressed through a determination under section 781A as to whether a particular type of merchandise is within the class or kind of merchandise described in an existing finding of dumping or an antidumping or countervailing duty order. (B) Extension The administering authority may extend the deadline under subparagraph (A) by a period not to exceed 15 days if an interested party has placed information on the record in response to the request for a circumvention inquiry. (4) Determinations (A) Preliminary determinations (i) In general Except as provided in clause (ii), not later than 150 days after the date on which the administering authority initiates a circumvention inquiry under paragraph (1) or (3)(A), the administering authority shall make a preliminary determination, based on the information available to it at the time of the determination, of whether there is a reasonable basis to believe or suspect that the merchandise subject to the inquiry is circumventing an existing finding of dumping or an antidumping or countervailing duty order. (ii) Extension The administering authority may extend the deadline under clause (i) by a period not to exceed 60 days. (B) Final determinations (i) In general Except as provided in clause (ii), not later than 150 days after issuing a preliminary determination under subparagraph (A) with respect to a circumvention inquiry, the administering authority shall make a final determination of whether the merchandise subject to the inquiry is circumventing an existing finding of dumping or an antidumping or countervailing duty order. (ii) Extension The administering authority may extend the deadline under clause (i) by a period not to exceed 65 days. (C) Other class or kind determinations If an inquiry request under paragraph (2)(A) is addressed through a class or kind determination under section 781A, the administering authority shall make such determination not later than 335 days after the filing of the inquiry request. (5) Rule of construction Nothing in this section shall be construed to prevent the administering authority from simultaneously initiating a circumvention inquiry under paragraph (1) or (3)(A) and issuing a preliminary determination under paragraph (4)(A). .\n##### (b) Suspension of liquidation and collection of deposits of entries subject to circumvention inquiry\nSection 781 of the Tariff Act of 1930 is further amended by adding at the end the following:\n(g) Suspension of liquidation and collection of deposits of entries subject to circumvention inquiry (1) Initiation If the administering authority initiates a circumvention inquiry under paragraph (1) or (3)(A) of subsection (f), for each unliquidated entry of merchandise subject to the circumvention inquiry that was already subject to the suspension of liquidation, the administering authority shall order\u2014 (A) the continued suspension of liquidation of such entry; and (B) the continued posting of a cash deposit, at the prevailing all-others or country-wide rate, for each such entry. (2) Preliminary determination If the administering authority issues a preliminary affirmative determination under paragraph (4)(A) of subsection (f) with respect to a circumvention inquiry initiated under paragraph (1) or (3)(A) of that subsection, the administering authority shall order\u2014 (A) the continued suspension of liquidation for each unliquidated entry of merchandise subject to the circumvention inquiry that was already subject to the suspension of liquidation; (B) the suspension of liquidation for each unliquidated entry of merchandise subject to the circumvention inquiry not yet suspended that is entered, or withdrawn from warehouse, for consumption on or after the date of publication of the notice of initiation of the circumvention inquiry; (C) the suspension of liquidation for each entry of merchandise subject to the circumvention inquiry not yet suspended that is entered, or withdrawn from warehouse, for consumption before the date of publication of the notice of initiation of the circumvention inquiry if the administering authority determines, under the circumstances, that suspension under this subparagraph is warranted; and (D) the posting, or continued posting, of a cash deposit in an amount equal to the antidumping duty or countervailing duty applicable for each entry of merchandise described in subparagraph (A), (B), or (C). (3) Final determination If the administering authority issues a final affirmative determination under paragraph (4)(B) of subjection (f) with respect to a circumvention inquiry initiated under paragraph (1) or (3)(A) of that subsection, the administering authority shall order\u2014 (A) the continued suspension of liquidation for each unliquidated entry of merchandise subject to the circumvention inquiry that was already subject to the suspension of liquidation; (B) the suspension of liquidation of each entry of merchandise subject to the circumvention inquiry that is entered, or withdrawn from warehouse, for consumption on or after the date of publication of the notice of initiation of the circumvention inquiry; (C) the suspension of liquidation of each entry of merchandise subject to the circumvention inquiry that is entered, or withdrawn from warehouse, for consumption before the date of publication of the notice of initiation of circumvention inquiry if the administering authority determines, under the circumstances, that suspension under this subparagraph is warranted; and (D) the posting, or continued posting, of a cash deposit in an amount equal to the antidumping duty or countervailing duty applicable for each entry of merchandise described in subparagraph (A), (B), or (C). (4) Rule of construction Nothing in this section shall be construed to prevent the administering authority from applying the requirements under this subsection in a class or kind determination under section 781A. (h) Application of circumvention determination (1) In general The administering authority shall consider the appropriate remedy to address circumvention and prevent evasion of an order or finding pursuant to an affirmative determination under subparagraph (A) or (B) of subsection (f)(4). (2) Remedies considered Remedies considered under paragraph (1) may include the following: (A) The application of the determination described in paragraph (1) on a producer-specific, exporter-specific, or importer-specific basis, or some combination thereof, and, as the administering authority determines appropriate, the implementation of a certification requirement under section 785. (B) The application of the determination described in paragraph (1) on a countrywide basis to all merchandise from a particular country, regardless of producer, exporter, or importer of that merchandise, and, as the administering authority determines appropriate, the implementation of a certification requirement under section 785. (3) Exemption for merchandise under certification If a certification requirement under section 785 is implemented under this subsection and the importer or other party to which the requirement is applied complies with that requirement, antidumping and countervailing duties under this title may not be applied to the merchandise under certification. .\n##### (c) Publication in the Federal Register\nSection 777(i) of the Tariff Act of 1930 ( 19 U.S.C. 1677f(i) ) is amended by adding at the end the following:\n(4) Circumvention inquiries Whenever the administering authority makes a determination under section 781 whether to initiate a circumvention inquiry or makes a preliminary or final determination under subsection (f)(4) of that section, the administering authority shall publish the facts and conclusions supporting that determination and shall publish notice of that determination in the Federal Register. .\n##### (d) Adding verification responses in circumvention inquiries\nSection 782(i) of the Tariff Act of 1930 ( 19 U.S.C. 1677m(i) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking and at the end;\n**(2)**\nin paragraph (3)(B), by striking the period at the end and inserting , and ; and\n**(3)**\nby adding at the end the following:\n(4) a final determination in a circumvention inquiry conducted pursuant to section 781 if good cause for verification is shown. .\n#### 302. Requirement of provision by importer of certification by importer or other party\n##### (a) In general\nSubtitle D of title VII of the Tariff Act of 1930 ( 19 U.S.C. 1677 et seq. ), as amended by section 103(a), is further amended by adding at the end the following:\n785. Requirement for certification by importer or other party (a) Requirement (1) In general For imports of merchandise into the customs territory of the United States, the administering authority may require an importer or other party\u2014 (A) to provide a certification described in paragraph (2) at the time of entry or with the entry summary; (B) to maintain that certification; or (C) to otherwise demonstrate compliance with the requirements for that certification. (2) Certification described A certification described in this paragraph is a certification by the importer of the merchandise or other party, as required by the administering authority, including a certification that\u2014 (A) the merchandise is not subject to an antidumping or countervailing duty proceeding under this title; and (B) the inputs used in production, transformation, or processing of the merchandise are not subject to an antidumping or countervailing duty under this title. (3) Available upon request A certification required by the administering authority under paragraph (1), if not already provided, shall be made available upon request to the administering authority or the Commissioner of U.S. Customs and Border Protection (in this section referred to as the Commissioner ). (b) Authority To suspend liquidation, collect cash deposits and assess duties (1) In general If the administering authority requires an importer or other party to provide a certification described in paragraph (2) of subsection (a) for merchandise imported into the customs territory of the United States pursuant to paragraph (1) of that subsection, and the importer or other party does not provide that certification or that certification contains any false, misleading, or fraudulent statement or representation or any material omission, the administering authority shall instruct the Commissioner\u2014 (A) to suspend liquidation of the entry; (B) to require that the importer or other party post a cash deposit in an amount equal to the antidumping duty or countervailing duty applicable to the merchandise; and (C) to assess the appropriate rate of duty upon liquidation or reliquidation of the entry. (2) Assessment rate If no rate of duty for an entry is available at the time of assessment under paragraph (1)(C), the administering authority shall identify the applicable cash deposit rate to be applied to the entry, with the applicable duty rate to be provided as soon as the duty rate becomes available. (c) Penalties If the administering authority requires an importer or other party to provide a certification described in paragraph (2) of subsection (a) for merchandise imported into the customs territory of the United States pursuant to paragraph (1) of that subsection, and the importer or other party does not provide that certification or that certification contains any false, misleading, or fraudulent statement or representation or any material omission, the importer of the merchandise may be subject to a penalty pursuant to section 592 of this Act, section 1001 of title 18, United States Code, or any other applicable provision of law. .\n##### (b) Clerical amendment\nThe table of contents for the Tariff Act of 1930, as amended by section 103(b), is further amended by inserting after the item relating to section 784 the following:\nSec. 785. Requirement for certification by importer or other party. .\n#### 303. Clarification of authority for Department of Commerce regarding merchandise covered by antidumping and countervailing duty proceedings\n##### (a) In general\nSubtitle D of title VII of the Tariff Act of 1930 ( 19 U.S.C. 1677 et seq. ) is amended by inserting after section 781 the following:\n781A. Determinations of merchandise covered under antidumping or countervailing duty proceeding (a) In general To determine whether merchandise imported into the United States is covered by an antidumping or countervailing duty proceeding under this title, the administering authority may use any reasonable method and is not bound by the determinations of any other Federal agency, including tariff classification and country of origin marking rulings issued by the Commissioner of U.S. Customs and Border Protection. (b) Class or kind of merchandise For purposes of this title, determinations regarding whether merchandise is the same class or kind may be made under this section or under section 781 in accordance with the criteria set forth in this section or in section 781, as the case may be. (c) Origin of merchandise To determine the origin of merchandise for purposes of an antidumping or countervailing duty proceeding under this title, the administering authority may apply any reasonable method and may consider relevant factors, including\u2014 (1) whether the processed downstream product is a different class or kind of merchandise than the upstream product; (2) the physical characteristics of the merchandise; (3) the intended end use of the downstream product; (4) the cost of production and the value added of further processing in a third country or countries; (5) the nature and sophistication of processing in a third country or countries; (6) the level of investment in a third country or countries; and (7) any other factors that the administering authority considers appropriate, including whether an essential characteristic of the merchandise, or an essential component thereof, is substantially transformed in the country of exportation. .\n##### (b) Clerical amendment\nThe table of contents for the Tariff Act of 1930 is amended by inserting after the item relating to section 781 the following:\nSec. 781A. Determinations of merchandise covered under antidumping or countervailing duty proceeding. .\n##### (c) Reviewable determinations\nSection 516A(a)(2)(A) of the Tariff Act of 1930 ( 19 U.S.C. 1516a(a)(2)(A) ) is amended\u2014\n**(1)**\nin clause (i)(I), by striking (iv), ; and\n**(2)**\nby amending clause (ii) to read as follows:\n(ii) the date of publication in the Federal Register of notice of a determination described in clause (iv) of subparagraph (B) or, if no such notice is published, the date on which the administering authority conveys a copy of such determination to an interested party who is a party to the proceeding, .\n#### 304. Asset requirements applicable to nonresident importers\n##### (a) In general\nPart III of title IV of the Tariff Act of 1930 ( 19 U.S.C. 1481 et seq. ) is amended by inserting after section 484b the following:\n484c. Asset requirements applicable to nonresident importers (a) Definitions In this section: (1) Importer; nonresident importer The terms importer and nonresident importer have the meanings given those terms in section 641(i). (2) Resident importer The term resident importer means any importer other than a nonresident importer. (b) Requirements for nonresident importers Except as provided in subsection (c), the Commissioner of U.S. Customs and Border Protection shall\u2014 (1) require a nonresident importer that imports merchandise into the United States to maintain assets in the United States sufficient to pay all duties that may potentially be applied to the merchandise; and (2) require a bond with respect to the merchandise in an amount sufficient to ensure full liability on the part of a nonresident importer and the surety of the importer based on the amount of assets the Commissioner determines to be sufficient under subsection (c). (c) Determination of amount of assets required To Be maintained For purposes of subsection (b)(1), the Commissioner shall calculate the amount of assets sufficient to pay all duties that may potentially be applied to merchandise imported by a nonresident importer based on an amount that exceeds the amount, calculated using the fair market value of the merchandise, of all duties, fees, interest, taxes, or other charges, and all deposits for duties, fees, interest, taxes, or other charges, that would apply with respect to the merchandise if the merchandise were subject to the highest rate of duty applicable to such merchandise imported from any country. (d) Maintenance of assets in the United States (1) In general For purposes of subsection (b)(1), a nonresident importer of merchandise meets the requirement to maintain assets in the United States if the importer has clear title, at all times between the entry of the merchandise and the liquidation of the entry, to assets described in paragraph (2) with a value equal to the amount determined under subsection (c). (2) Assets described An asset described in this paragraph is\u2014 (A) an asset held by a United States financial institution; (B) an interest in an entity organized under the laws of the United States or any jurisdiction within the United States; or (C) an interest in real or personal property located in the United States or any territory or possession of the United States. (e) Exceptions The requirements of this section shall not apply with respect to a nonresident importer\u2014 (1) that is a validated Tier 2 or Tier 3 participant in the Customs-Trade Partnership Against Terrorism program established under subtitle B of title II of the Security and Accountability For Every Port Act of 2006 ( 6 U.S.C. 961 et seq. ); or (2) if the Commissioner is satisfied, based on certified information supplied by the importer and any other relevant evidence, that the Commissioner has the same or equivalent ability to collect all duties that may potentially be applied to merchandise imported by the importer as the Commissioner would have if the importer were a resident importer. (f) Procedures The Commissioner shall prescribe procedures for assuring that nonresident importers maintain the assets required by subsection (b). (g) Penalties (1) In general It shall be unlawful for any person to import into the United States any merchandise in violation of this section. (2) Civil penalties Any person who violates paragraph (1) shall\u2014 (A) in the case of merchandise described in such paragraph with a domestic value that is equal to or greater than $50,000, be liable for a civil penalty of $50,000 for each such violation; or (B) in the case of merchandise described in such paragraph with a domestic value that is less than $50,000, be liable for a civil penalty equal to 50 percent of the amount of such domestic value for each such violation. (3) Other penalties In addition to the penalties specified in paragraph (2), any violation of this section that violates any other provision of the customs and trade laws of the United States (as defined in section 2 of the Trade Facilitation and Trade Enforcement Act of 2015 ( 19 U.S.C. 4301 )) shall be subject to any applicable civil or criminal penalty, including seizure and forfeiture, that may be imposed under that provision or title 18, United States Code. .\n##### (b) Clerical amendment\nThe table of contents for the Tariff Act of 1930 is amended by inserting after the item relating to section 484b the following:\nSec. 484c. Asset requirements applicable to nonresident importers. .\n##### (c) Effective date and application\n**(1) In general**\nSection 484c of the Tariff Act of 1930, as added by subsection (a)\u2014\n**(A)**\ntakes effect on the date of the enactment of this Act; and\n**(B)**\napplies with respect to merchandise entered, or withdrawn from warehouse for consumption, on or after the date that is 180 days after such date of enactment.\n**(2) Deadline for procedures**\nThe Commissioner of U.S. Customs and Border Protection shall ensure the procedures required under subsection (f) of section 484c of the Tariff Act of 1930, as added by subsection (a), are prescribed and in effect not later than 90 days after the date of the enactment of this Act.\nIV\nCountering currency undervaluation\n#### 401. Investigation or review of currency undervaluation under countervailing duty law\nSection 702(c) of the Tariff Act of 1930 ( 19 U.S.C. 1671a(c) ) is amended by adding at the end the following:\n(6) Currency undervaluation For purposes of a countervailing duty investigation under this subtitle in which the determinations under clauses (i) and (ii) of paragraph (1)(A) are affirmative and the petition includes an allegation of currency undervaluation by the government of a country or any public entity within the territory of a country that meets the requirements of clause (i) of that paragraph, or for purposes of a review under subtitle C with respect to a countervailing duty order involving such an allegation, the administering authority shall examine in its investigation or review whether currency undervaluation by the government of a country or any public entity within the territory of a country is providing, directly or indirectly, a countervailable subsidy. .\n#### 402. Determination of benefit with respect to currency undervaluation\nSection 771(5)(E) of the Tariff Act of 1930 ( 19 U.S.C. 1677(5)(E) ) is amended\u2014\n**(1)**\nin clause (iii), by striking , and and inserting a comma;\n**(2)**\nin clause (iv), by striking the period at the end and inserting , and ;\n**(3)**\nby inserting after clause (iv) the following:\n(v) in the case of an exchange of an undervalued currency under a unified exchange rate, if there is a difference between the amount of currency received in exchange for United States dollars and the amount of currency that the recipient would have received absent an undervalued currency. ; and\n**(4)**\nin the flush text following clause (v), as added by paragraph (3), by adding at the end the following: For purposes of clause (v), a determination of the existence and amount of a benefit from the exchange of an undervalued currency shall take into account a comparison of the exchange rates derived from a methodology determined by the administering authority to be appropriate in light of the facts and circumstances to the relevant actual exchange rates, and whether there is government action on the exchange rate that contributes to an undervaluation of the currency. .\nV\nPreventing duty evasion\n#### 501. Limitation on protest against decisions of U.S. Customs and Border Protection of claims of evasion of antidumping and countervailing duty orders\n##### (a) Expansion of limitation\nSection 514(b) of the Tariff Act of 1930 ( 19 U.S.C. 1514(b) ) is amended\u2014\n**(1)**\nby striking title, determinations and inserting title, or with respect to determinations made under section 517 of this title which are reviewable under section 517(g), determinations ; and\n**(2)**\nby inserting after a determination listed in section 516A of this title the following: or a determination listed in section 517 of this title, as the case may be, .\n##### (b) Rule of construction on investigation of claims of evasion\nSection 517(h) of the Tariff Act of 1930 ( 19 U.S.C. 1517(h) ) is amended by inserting before the period at the end the following: , except that any decision as to the liquidation or reliquidation of an entry of covered merchandise in accordance with a determination under subsection (c) and review under subsection (f), if applicable, shall not be subject to a protest of such decision filed in accordance with section 514 .\n#### 502. Procedures for investigating claims of evasion of safeguard actions\n##### (a) Tariff Act of 1930\nSection 517 of the Tariff Act of 1930 ( 19 U.S.C. 1517 ) is amended\u2014\n**(1)**\nin the section heading, by inserting and safeguard actions after orders ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking or at the end;\n**(ii)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following:\n(C) an action taken under section 203 of the Trade Act of 1974 ( 19 U.S.C. 2253 ). ; and\n**(B)**\nin paragraph (5)(A), by inserting after applicable antidumping or countervailing duties the following: or any applicable safeguard action ;\n**(3)**\nin subsection (b)(4), in subparagraphs (A) and (B), by inserting after covered merchandise each place it appears the following: under subparagraph (A) or (B) of subsection (a)(3) ;\n**(4)**\nin subsection (d)(1)\u2014\n**(A)**\nin subparagraph (C)\u2014\n**(i)**\nin the matter preceding clause (i), by inserting after (C) the following: if the determination relates to covered merchandise under subparagraph (A) or (B) of subsection (a)(3), ; and\n**(ii)**\nin clause (i), by inserting of this paragraph after subparagraphs (A) and (B) ; and\n**(B)**\nin subparagraph (D)\u2014\n**(i)**\nby inserting after (D) the following: if the determination relates to covered merchandise under subparagraph (A) or (B) of subsection (a)(3), ; and\n**(ii)**\nby inserting of this paragraph after subparagraphs (A) and (B) .\n##### (b) Trade Facilitation and Trade Enforcement Act of 2015\nThe Trade Facilitation and Trade Enforcement Act of 2015 is amended\u2014\n**(1)**\nin section 402 ( 19 U.S.C. 4361 )\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking or at the end;\n**(ii)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following:\n(C) an action taken under section 203 of the Trade Act of 1974 ( 19 U.S.C. 2253 ). ;\n**(B)**\nin paragraph (5), by inserting after applicable antidumping or countervailing duties the following: or any applicable safeguard action ; and\n**(C)**\nin paragraph (7), by inserting before the period at the end the following: and chapter 1 of title II of the Trade Act of 1974 ( 19 U.S.C. 2251 et seq. ) ; and\n**(2)**\nin section 412 ( 19 U.S.C. 4372 )\u2014\n**(A)**\nin subsection (a)(2)\u2014\n**(i)**\nby redesignating subparagraphs (A), (B), and (C) as subparagraphs (B), (C), and (D), respectively; and\n**(ii)**\nby inserting before subparagraph (B), as redesignated by clause (i), the following:\n(A) a person reasonably suspected of entering covered merchandise into the customs territory of the United States through evasion; ; and\n**(B)**\nin subsection (b)(1)\u2014\n**(i)**\nin subparagraph (B)\u2014\n**(I)**\nby redesignating clauses (i), (ii), and (iii) as clauses (ii), (iii), and (iv), respectively; and\n**(II)**\nby inserting before clause (ii), as redesignated by subclause (I), the following:\n(i) a person from whom information was requested pursuant to subsection (a)(2)(A); ; and\n**(ii)**\nin subparagraph (C), by striking clause (ii) or (iii) and inserting clause (i), (iii), or (iv) .\n#### 503. Application of provisions relating to certain proprietary information\n##### (a) In general\nSection 517 of the Tariff Act of 1930 ( 19 U.S.C. 1517 ), as amended by section 502(a), is further amended by adding at the end the following:\n(i) Application of provisions relating to certain proprietary information (1) In general Except as provided in paragraph (2), subsections (b), (c), and (d) of section 777, relating to information submitted in connection with proceedings under title VII, shall apply with respect to information submitted in connection with proceedings under this section to the same extent and in the same manner as those subsections may apply to information submitted in connection with proceedings under title VII. (2) Exceptions In carrying out paragraph (1), subsections (b), (c), and (d) of section 777 shall be applied and administered as follows: (A) By substituting the Commissioner for each of the following terms each place those terms appear: (i) the administering authority or the Commission . (ii) the administering authority and the Commission . (iii) the administering authority . (B) Paragraphs (1)(A) and (3) of such subsection (b) shall not apply. (C) The second and third sentences of such subsection (c)(1)(A) shall not apply. (D) In such subsection (c)\u2014 (i) in paragraph (1)\u2014 (I) in subparagraph (B), by substituting determine to be appropriate for determine to be appropriate, including disbarment from practice before the agency ; and (II) in subparagraph (C)\u2014 (aa) in clause (i), by substituting 14 days for 14 days (7 days if the submission pertains to a proceeding under section 703(a) or 733(a)) ; and (bb) in the text following clause (ii)(II), by substituting 30 days for 30 days (10 days if the submission pertains to a proceeding under section 703(a) or 733(a)) ; and (ii) in paragraph (2), by substituting United States Court of International Trade for United States Customs Court . .\n##### (b) Regulations\nThe Commissioner of U.S. Customs and Border Protection shall prescribe such regulations as may be necessary to implement subsection (i) of section 517 of the Tariff Act of 1930 ( 19 U.S.C. 1517 ), as added by subsection (a).\n##### (c) Effective date\nThe amendment made by subsection (a) shall take effect on the date that is 180 days after the date of the enactment of this Act.\nVI\nGeneral provisions\n#### 601. Application to Canada and Mexico\nPursuant to section 418 of the United States-Mexico-Canada Agreement Implementation Act ( 19 U.S.C. 4588 ), the amendments made by this Act apply with respect to goods from Canada and Mexico.\n#### 602. Effective date\n##### (a) In general\nExcept as provided by subsection (b) or (c), the amendments made by this Act apply to countervailing duty investigations initiated under subtitle A of title VII of the Tariff Act of 1930 ( 19 U.S.C. 1671 et seq. ), antidumping duty investigations initiated under subtitle B of title VII of such Act ( 19 U.S.C. 1673 et seq. ), reviews initiated under subtitle C of title VII of such Act ( 19 U.S.C. 1675 et seq. ), and circumvention inquiries requested under section 781 of such Act ( 19 U.S.C. 1677j ), on or after the date of the enactment of this Act.\n##### (b) Applicability\n**(1) In general**\nExcept as provided in subsection (c), the amendments made by this Act apply to\u2014\n**(A)**\ninvestigations or reviews under title VII of the Tariff Act of 1930 ( 19 U.S.C. 1671 et seq. ) pending on the date of the enactment of this Act if the date on which the fully extended preliminary determination is scheduled is not earlier than 45 days after such date of enactment;\n**(B)**\ncircumvention inquiries initiated under section 781 of such Act ( 19 U.S.C. 1677j ) before and pending on such date of enactment; and\n**(C)**\ncircumvention inquiries requested under section 781 of such Act but not initiated before such date of enactment.\n**(2) Deadlines for circumvention inquiries**\n**(A) Determinations**\nIn this case of a circumvention inquiry described in paragraph (1)(B), subsection (f)(4) of section 781 of the Tariff Act of 1930 ( 19 U.S.C. 1677j ), as amended by section 301(a), shall be applied and administered\u2014\n**(i)**\nin subparagraph (A)(i), by substituting the date of the enactment of the Leveling the Playing Field 2.0 Act for the date on which the administering authority initiates a circumvention inquiry under paragraph (1) or (3)(A) ; and\n**(ii)**\nin subparagraph (C), by substituting the date of the enactment of the Leveling the Playing Field 2.0 Act for the filing of the inquiry request .\n**(B) Actions with respect to inquiry requests**\nIn the case of a circumvention inquiry described in paragraph (1)(C), the administering authority (as defined in section 771(1) of the Tariff Act of 1930 ( 19 U.S.C. 1677(1) )) shall, not later than 20 days after the date of the enactment of this Act, take an action described in subsection (f)(3) of section 781 of the Tariff Act of 1930 ( 19 U.S.C. 1677j ), as amended by section 301(a), with respect to the inquiry.\n##### (c) Retroactive application of provision on determination of normal value To account for distortions of costs that occur in foreign countries\nThe amendments made by section 204 apply to\u2014\n**(1)**\nantidumping duty investigations initiated under subtitle B of title VII of the Tariff Act of 1930 ( 19 U.S.C. 1673 et seq. ) on or after June 29, 2015;\n**(2)**\nreviews initiated under subtitle C of title VII of such Act ( 19 U.S.C. 1675 et seq. ) on or after June 29, 2015;\n**(3)**\nactions by U.S. Customs and Border Protection resulting from an investigation specified in paragraph (1) or a review specified in paragraph (2); and\n**(4)**\ncivil actions, criminal proceedings, and other proceedings before a Federal court relating to proceedings specified in paragraph (1) or (2) or actions specified to in paragraph (3) in which final judgment has not been entered on or before the date of the enactment of this Act.",
      "versionDate": "2025-02-24",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-24",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1548",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Leveling the Playing Field 2.0 Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-07-17T19:33:36Z"
          },
          {
            "name": "Canada",
            "updateDate": "2025-07-17T19:33:36Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-07-17T19:33:36Z"
          },
          {
            "name": "Competitiveness, trade promotion, trade deficits",
            "updateDate": "2025-07-17T19:33:36Z"
          },
          {
            "name": "Currency",
            "updateDate": "2025-07-17T19:33:36Z"
          },
          {
            "name": "Customs enforcement",
            "updateDate": "2025-07-17T19:33:36Z"
          },
          {
            "name": "Foreign and international corporations",
            "updateDate": "2025-07-17T19:33:36Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-07-17T19:33:37Z"
          },
          {
            "name": "Free trade and trade barriers",
            "updateDate": "2025-07-17T19:33:37Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-17T19:33:36Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-17T19:33:37Z"
          },
          {
            "name": "International monetary system and foreign exchange",
            "updateDate": "2025-07-17T19:33:36Z"
          },
          {
            "name": "Mexico",
            "updateDate": "2025-07-17T19:33:36Z"
          },
          {
            "name": "North America",
            "updateDate": "2025-07-17T19:33:37Z"
          },
          {
            "name": "Tariffs",
            "updateDate": "2025-07-17T19:33:37Z"
          },
          {
            "name": "Trade agreements and negotiations",
            "updateDate": "2025-07-17T19:33:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-06-24T18:29:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
    "originChamber": "Senate",
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
          "measure-id": "id119s691",
          "measure-number": "691",
          "measure-type": "s",
          "orig-publish-date": "2025-02-24",
          "originChamber": "SENATE",
          "update-date": "2026-05-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s691v00",
            "update-date": "2026-05-11"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Leveling the Playing Field 2.0 Act</strong></p><p>This bill addresses unfair trade practices by making various changes to U.S. antidumping and countervailing duty laws. Antidumping laws provide relief to U.S industries and workers that are materially injured or threatened with injury due to imports of like products sold in the U.S. market at less than fair value, while countervailing duty laws provide such relief from imports of products subsidized by a foreign government or public entity.</p><p>Specifically, the bill establishes a process for successive antidumping and countervailing duty investigations. Successive investigations may be concurrent (an ongoing investigation of the same product) or recently completed (not more than two years before the date of the initiation of the successive investigation). Further, the bill establishes a timeline for the Department of Commerce to issue determinations in successive investigations.</p><p>Among other provisions, the bill authorizes Commerce to</p><ul><li>apply countervailing duty law to subsidies provided by a foreign government or public entity to a company operating in a different country,</li><li>use another method for calculating the cost of production in specific circumstances, and</li><li>require importers to certify\u00a0that the imported merchandise is not subject to an antidumping or countervailing duty order.</li></ul><p>Additionally, the bill statutorily establishes procedures for Commerce to conduct circumvention inquiries, including by specifying the deadlines for preliminary and final determinations.</p><p>The bill also provides statutory authority for Commerce to investigate currency undervaluation as a countervailable subsidy.</p>"
        },
        "title": "Leveling the Playing Field 2.0 Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s691.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Leveling the Playing Field 2.0 Act</strong></p><p>This bill addresses unfair trade practices by making various changes to U.S. antidumping and countervailing duty laws. Antidumping laws provide relief to U.S industries and workers that are materially injured or threatened with injury due to imports of like products sold in the U.S. market at less than fair value, while countervailing duty laws provide such relief from imports of products subsidized by a foreign government or public entity.</p><p>Specifically, the bill establishes a process for successive antidumping and countervailing duty investigations. Successive investigations may be concurrent (an ongoing investigation of the same product) or recently completed (not more than two years before the date of the initiation of the successive investigation). Further, the bill establishes a timeline for the Department of Commerce to issue determinations in successive investigations.</p><p>Among other provisions, the bill authorizes Commerce to</p><ul><li>apply countervailing duty law to subsidies provided by a foreign government or public entity to a company operating in a different country,</li><li>use another method for calculating the cost of production in specific circumstances, and</li><li>require importers to certify\u00a0that the imported merchandise is not subject to an antidumping or countervailing duty order.</li></ul><p>Additionally, the bill statutorily establishes procedures for Commerce to conduct circumvention inquiries, including by specifying the deadlines for preliminary and final determinations.</p><p>The bill also provides statutory authority for Commerce to investigate currency undervaluation as a countervailable subsidy.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119s691"
    },
    "title": "Leveling the Playing Field 2.0 Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Leveling the Playing Field 2.0 Act</strong></p><p>This bill addresses unfair trade practices by making various changes to U.S. antidumping and countervailing duty laws. Antidumping laws provide relief to U.S industries and workers that are materially injured or threatened with injury due to imports of like products sold in the U.S. market at less than fair value, while countervailing duty laws provide such relief from imports of products subsidized by a foreign government or public entity.</p><p>Specifically, the bill establishes a process for successive antidumping and countervailing duty investigations. Successive investigations may be concurrent (an ongoing investigation of the same product) or recently completed (not more than two years before the date of the initiation of the successive investigation). Further, the bill establishes a timeline for the Department of Commerce to issue determinations in successive investigations.</p><p>Among other provisions, the bill authorizes Commerce to</p><ul><li>apply countervailing duty law to subsidies provided by a foreign government or public entity to a company operating in a different country,</li><li>use another method for calculating the cost of production in specific circumstances, and</li><li>require importers to certify\u00a0that the imported merchandise is not subject to an antidumping or countervailing duty order.</li></ul><p>Additionally, the bill statutorily establishes procedures for Commerce to conduct circumvention inquiries, including by specifying the deadlines for preliminary and final determinations.</p><p>The bill also provides statutory authority for Commerce to investigate currency undervaluation as a countervailable subsidy.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119s691"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s691is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Leveling the Playing Field 2.0 Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Leveling the Playing Field 2.0 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Tariff Act of 1930 to improve the administration of antidumping and countervailing duty laws, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:03:22Z"
    }
  ]
}
```
