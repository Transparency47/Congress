# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/735?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/735
- Title: United States Reciprocal Trade Act
- Congress: 119
- Bill type: HR
- Bill number: 735
- Origin chamber: House
- Introduced date: 2025-01-24
- Update date: 2025-07-03T15:20:21Z
- Update date including text: 2025-07-03T15:20:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-24 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-24: Introduced in House

## Actions

- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-24 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/735",
    "number": "735",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001235",
        "district": "2",
        "firstName": "Riley",
        "fullName": "Rep. Moore, Riley [R-WV-2]",
        "lastName": "Moore",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "United States Reciprocal Trade Act",
    "type": "HR",
    "updateDate": "2025-07-03T15:20:21Z",
    "updateDateIncludingText": "2025-07-03T15:20:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-24T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "GA"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "GA"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NC"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "AZ"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "GA"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "GA"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas [R-AK-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "AK"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "OH"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr735ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 735\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 24, 2025 Mr. Moore of West Virginia (for himself, Ms. Greene of Georgia , Mr. Collins , Mr. McDowell , Mr. Hamadeh of Arizona , Mr. Loudermilk , Mr. Jack , Mr. Begich , and Mr. Rulli ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the President to take certain actions relating to reciprocal trade, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States Reciprocal Trade Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe United States maintains an open market for goods, with relatively low tariffs, and has long encouraged trading partners, both bilaterally and in multilateral fora, to liberalize their markets.\n**(2)**\nThe United States is the world\u2019s largest importer of goods.\n**(3)**\nTrading partners of the United States in many instances impose significantly higher tariffs on United States goods than the United States imposes on the same or similar goods imported from those same countries.\n**(4)**\nEuropeans have continued to protect their auto markets from United States automotive companies through high tariffs while dumping cheap European cars into the United States, undermining our automotive industry.\n**(5)**\nCanadian and Mexican authorities have flooded American markets with cheap goods while simultaneously allowing for illegal migrants and poisonous fentanyl to pour into the United States.\n**(6)**\nUnited States trading partners in many instances impose significant nontariff barriers that greatly undermine the value of negotiated tariff concessions.\n**(7)**\nThe lack of reciprocity in tariff levels and disproportionate use of nontariff barriers by United States trading partners facilitates foreign imports, discourages United States exports, and puts United States producers, farmers, and workers at a competitive disadvantage.\n**(8)**\nThe lack of reciprocity in tariff levels and nontariff barriers contributes to the large and growing United States trade deficit in goods, which is a drag on economic growth and undermines economic prosperity.\n**(9)**\nTariffs under the Trump presidency substantially shrank the trade deficit with China.\n**(10)**\nThe President must be able to levy tariffs on our global competitors. Preferential treatment of adversaries, such as China\u2019s Most Favored Nation trading status, undermines American national security interests domestically and around the world.\n**(11)**\nTo date a number of United States trading partners have been unwilling, including in multilateral negotiations, to reduce tariffs and eliminate nontariff barriers applied to United States exports.\n**(12)**\nThe United States should seek action by United States trading partners to lower tariffs and eliminate nontariff barriers, to promote efficiency in those markets and enhance opportunities for United States producers, farmers, and workers.\n**(13)**\nFor the United States to maintain its economic dominance globally, the President must have the authority to levy reciprocal tariffs against unfair trading partners.\n**(14)**\nThe President should have a wide array of tools to open the markets of United States trading partners and encourage participation in negotiations to liberalize trade in goods on a fair and reciprocal basis, including the authority to adjust tariff rates to reciprocal levels.\n#### 3. Authority to take certain actions relating to reciprocal trade\n##### (a) In general\nIf the President determines that\u2014\n**(1)**\nthe rate of duty imposed by a foreign country with respect to a particular good, when imported from the United States, is significantly higher than the rate of duty imposed by the United States on that good, when imported from that country, or\n**(2)**\nthe nontariff barriers applied by a foreign country with respect to a particular good, when imported from the United States, impose significantly higher burdens, alone or in combination with any tariffs imposed by that country on that good, than the burdens of the nontariff barriers applied by the United States with respect to that good, alone or in combination with any tariffs imposed by the United States on that good, when imported from that country,\nthe President may take one or more of the actions authorized under subsection (b).\n##### (b) Actions authorized\nThe actions authorized under this subsection are the following:\n**(1)**\nTo negotiate and seek to enter into an agreement with the foreign country that commits the country to reduce the rate of duty or reduce or eliminate nontariff barriers on the good that is the subject of the determination under subsection (a).\n**(2)**\nTo impose a rate of duty on imports of the good that is equal to\u2014\n**(A)**\nthe rate of duty imposed by the foreign country with respect to the good, in the case of a determination described in subsection (a)(1); or\n**(B)**\nthe effective rate of duty of the nontariff barriers applied by the foreign country with respect to the good, alone or in combination with any tariffs imposed by that country on that good, in the case of a determination described in subsection (a)(2).\n##### (c) Factors\nIn taking an action authorized under subsection (b), the President shall consider the following factors:\n**(1)**\nThe tariff classification of the good by the United States and the tariff classification of the good by the foreign country.\n**(2)**\nThe rate of duty applied by the United States with respect to the good and the rate of duty applied by the foreign country with respect to the good.\n**(3)**\nThe physical characteristics of the good.\n**(4)**\nThe end uses and existence of a competitive relationship between the good\u2014\n**(A)**\nas exported from the United States to the foreign country; and\n**(B)**\nas imported from the country to the United States.\n**(5)**\nThe level of exports of the good by the country to the United States and to other countries.\n**(6)**\nIn the case of a determination described in subsection (a)(1), the extent to which the rate of duty applied by the foreign country with respect to the good is impeding or distorting trade.\n**(7)**\nIn the case of a determination described in subsection (a)(2)\u2014\n**(A)**\nthe extent of the nontariff barriers applied by the foreign country with respect to the good and the extent of the nontariff barriers applied by the United States with respect to the good;\n**(B)**\nthe extent to which the nontariff barriers applied by the country with respect to the good, alone or in combination with any tariffs imposed by that country on that good, are impeding or distorting trade;\n**(C)**\nthe identified purpose of the nontariff barriers applied by the country with respect to the good, if any, and the extent to which the nontariff barriers are more restrictive than necessary to meet that purpose; and\n**(D)**\nthe degree of transparency of the process by which the country adopted the nontariff barriers.\n**(8)**\nOther factors, as the President determines appropriate.\n##### (d) Role of USTR\nThe United States Trade Representative, in consultation with the Secretary of Treasury, the Secretary of Commerce, and the heads of other relevant Federal agencies, shall advise the President in determining the effective rate of duty imposed by the nontariff barriers applied by a foreign country with respect to a good, alone or in combination with any tariffs imposed by that country on that good, in the case of a determination described in subsection (a)(2).\n##### (e) Lower rate of duty\nThe President may impose a rate of duty on imports of a good from a foreign country that is lower than the rate of duty described in subsection (b)(2)(A) or lower than the effective rate of duty described in subsection (b)(2)(B), as the case may be, if the President determines that application of such lower rate of duty is necessary and appropriate.\n##### (f) Higher rate of duty\nIf the President imposes a rate of duty on imports of a good from a foreign country under subsection (b)(2), and the country further increases its rate of duty on imports of the good from the United States, the President may further increase the rate of duty on imports of the good from the country to a rate that is equal to the rate of duty applied by that country.\n##### (g) Termination\nThe President shall terminate the imposition of any increase in the rate of duty on imports of a good from a foreign country under subsection (b)(2) effective on the date on which the President determines that\u2014\n**(1)**\nthe foreign country is no longer\u2014\n**(A)**\nimposing a rate of duty with respect to the good, as described in subsection (a)(1); or\n**(B)**\napplying nontariff barriers with respect to the good, as described in subsection (a)(2); or\n**(2)**\ncontinued imposition of the increased rate of duty on imports of the good from the foreign country is not in the economic or public interest of the United States.\n#### 4. Notice and consultation\n##### (a) In general\nBefore taking any action authorized under section 3(b)(1), the President shall provide notice to and consult with the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate regarding the proposed action.\n##### (b) Notice\nBefore taking any action authorized under section 3(b)(2), the President shall\u2014\n**(1)**\nnot less than 30 days before the date on which imposition of an increased rate of duty on imports of a good from a foreign country is to take effect, publish notice in the Federal Register of, and allow for public comment on, the proposed imposition and level of such increased rate of duty; and\n**(2)**\nseek advice regarding the proposed action from the advisory committees established under section 135 of the Trade Act of 1974 ( 19 U.S.C. 2155 ).\n##### (c) Additional notice\nThe President shall promptly publish in the Federal Register notice of any action taken pursuant to section 3(f) or 3(g).\n#### 5. Congressional disapproval of Presidential imposition of rates of duty on imports of goods from foreign countries under section 3(b)(2) ; disapproval resolution\n##### (a) In general\nAn action taken by the President under section 3(b)(2) to impose a rate of duty on imports of a good from a foreign country shall cease to have force and effect upon the enactment of a disapproval resolution, provided for in subsection (b), relating to that action.\n##### (b) Congressional rulemaking power; disapproval resolution\n**(1) In general**\nThis section is enacted by the Congress\u2014\n**(A)**\nas an exercise of the rulemaking power of the House of Representatives and the Senate, respectively, and as such is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedures to be followed in that House in the case of disapproval resolutions and such procedures supersede other rules only to the extent that they are inconsistent therewith; and\n**(B)**\nwith the full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as any other rule of that House.\n**(2) Disapproval resolution**\nFor purposes of this section, the term disapproval resolution means only a joint resolution of either House of Congress the matter after the resolving clause of which is as follows: That the Congress disapproves the action taken under section 3(b)(2) of the United States Reciprocal Trade Act with respect to the imposition of a rate of duty on imports of __ from __ under such section 3(b)(2). , the first blank space being filled with a description of the good with respect to which the duty is imposed under section 3(b)(2) and the second blank being filled with the name of the foreign country from which the good is imported into the United States.\n**(3) Consideration**\n**(A) Introduction**\nAll disapproval resolutions introduced in the House of Representatives shall be referred to the Committee on Ways and Means and all disapproval resolutions introduced in the Senate shall be referred to the Committee on Finance.\n**(B) Amendments prohibited; motions to suspend application of this subparagraph prohibited**\nNo amendment to a disapproval resolution shall be in order in either the House of Representatives or the Senate, and no motion to suspend the application of this subparagraph shall be in order in either House nor shall it be in order in either House for the Presiding Officer to entertain a request to suspend the application of this subparagraph by unanimous consent.\n**(C) Majority required for adoption**\nA disapproval resolution considered under this subsection shall require an affirmative vote of two-thirds of the Members, duly chosen and sworn, for adoption.\n#### 6. Report\nBefore entering into an agreement with a foreign country under section 3(b)(1), the United States Trade Representative shall submit to the appropriate congressional committees and leadership a report that describes\u2014\n**(1)**\nthe implementation of the agreement, including how it is consistent with and does not materially differ from or otherwise affect Federal or State laws or regulations;\n**(2)**\nthe impact on the competitiveness of United States businesses; and\n**(3)**\nthe impact on United States consumers.\n#### 7. Sunset of Presidential imposition of rates of duty on imports of goods from foreign countries under section 3(b)(2) by disapproval resolution\n##### (a) In general\nThe authority of the President to take an action under section 3(b)(2) to impose a rate of duty on imports of a good from a foreign country\u2014\n**(1)**\nshall be effective for the period ending on the date that is three years after the date of the enactment of this Act; and\n**(2)**\nshall be extended for an additional period of three years if (and only if)\u2014\n**(A)**\nthe President requests such extension under subsection (b); and\n**(B)**\na disapproval resolution is not enacted into law as provided for under subsection (c).\n##### (b) Report to Congress\nIf the President is of the opinion that the authority of the President to take an action under section 3(b)(2) to impose a rate of duty on imports of a good from a foreign country should be extended for the additional period described in subsection (a)(2), the President shall submit to Congress, not later than the date that is three months before the end of the period described in subsection (a)(1), a written report that contains a request for such extension, together with a description of all actions taken under section 3(b)(2) to date.\n##### (c) Disapproval resolution\n**(1) Congressional rulemaking power**\nThis section is enacted by the Congress\u2014\n**(A)**\nas an exercise of the rulemaking power of the House of Representatives and the Senate, respectively, and as such is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedures to be followed in that House in the case of disapproval resolutions and such procedures supersede other rules only to the extent that they are inconsistent therewith; and\n**(B)**\nwith the full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as any other rule of that House.\n**(2) Disapproval resolution**\nFor purposes of subsection (a), the term disapproval resolution means only a joint resolution of either House of Congress the matter after the resolving clause of which is as follows: That the Congress disapproves the request of the President for the extension, under section 7(a)(2)(A) of the United States Reciprocal Trade Act, of the authority of the President to take an action under section 3(b)(2) of such Act to impose a rate of duty on imports of a good from a foreign country after the period ending on the date that is three years after the date of the enactment of such Act. .\n**(3) Introduction; referral**\nA disapproval resolution\u2014\n**(A)**\nmay be introduced in either House of Congress by any member of such House; and\n**(B)**\nshall be referred, in the House of Representatives, to the Committee on Ways and Means and, in addition, to the Committee on Rules.\n**(4) Floor consideration**\nThe provisions of subsections (d) and (e) of section 152 of the Trade Act of 1974 ( 19 U.S.C. 2192 ) (relating to the floor consideration of certain resolutions in the House and Senate) apply to a disapproval resolution.\n**(5) Limitations on consideration**\nIt is not in order for\u2014\n**(A)**\nthe House of Representatives to consider any disapproval resolution not reported by the Committee on Ways and Means and, in addition, by the Committee on Rules;\n**(B)**\nthe Senate to consider any disapproval resolution not reported by the Committee on Finance; or\n**(C)**\neither House of Congress to consider a disapproval resolution after the date that is three years after the date of the enactment of this Act.\n##### (d) Rules of construction\n**(1) In general**\nAn action authorized under section 3(b)(2) to impose a rate of duty on imports of a good from a foreign country that is taken before the end of the period described in subsection (a)(1) or the end of the period described in subsection (a)(2) shall remain in effect after the end of such respective period.\n**(2) Additional authorities**\nThe President may exercise the authorities of subsections (e), (f), and (g) of section 3 with respect to an action described in paragraph (1) after the end of the period described in such paragraph that is applicable to such action.\n#### 8. Definitions\nIn this Act:\n**(1) Appropriate congressional committees and leadership**\nThe term appropriate congressional committees and leadership means\u2014\n**(A)**\nthe Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate; and\n**(B)**\nthe Speaker of the House of Representatives, the minority leader of the House of Representatives, the majority leader of the Senate, and the minority leader of the Senate.\n**(2) Nontariff barrier**\nThe term nontariff barrier includes any government-imposed measure or policy, other than a customs duty, that restricts, prevents, or impedes international trade in goods, including import policies, sanitary and phytosanitary measures, technical barriers to trade, government procurement, export subsidies, lack of intellectual property protection, digital trade barriers, and government-tolerated anticompetitive conduct of state-owned or private firms.\n**(3) Rate of duty**\nThe term rate of duty means the rate of customs duty applied on imports of a good, but does not include an antidumping or countervailing duty or a duty applied under a preferential tariff arrangement.",
      "versionDate": "2025-01-24",
      "versionType": "Introduced in House"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-06-20T18:34:59Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-20T18:34:48Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-06-20T18:34:53Z"
          },
          {
            "name": "Free trade and trade barriers",
            "updateDate": "2025-06-20T18:34:42Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-06-20T18:35:03Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-06-20T18:35:09Z"
          },
          {
            "name": "Tariffs",
            "updateDate": "2025-06-20T18:34:37Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-06-20T18:35:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-01T17:54:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119hr735",
          "measure-number": "735",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-24",
          "originChamber": "HOUSE",
          "update-date": "2025-07-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr735v00",
            "update-date": "2025-07-03"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>United States Reciprocal Trade Act </strong></p><p>This bill expands presidential trade authorities.</p><p>The bill allows the President, in certain circumstances, to (1) negotiate with a foreign country for tariff reductions on exported U.S. goods, or (2) impose additional duties on imported goods. Specifically, the President may take these actions if it is determined that the country (1) when importing a good from the United States, applies a higher rate of duty on that good than the rate imposed by the United States when the good is imported from that country; or (2) similarly imposes other,\u00a0nontariff trade restrictions on that good. This authority\u00a0shall be effective for three years, subject to a three-year renewal.</p><p>The President must terminate a rate of duty increase under this bill if the country no longer applies such higher rates or nontariff trade restrictions, or if the higher rate is no longer in the interest of the United States.</p><p>The bill also requires the President to consult with and notify Congress regarding the intention of the President to increase a rate of duty on imported goods.</p><p>Congress may nullify a rate of duty increase implemented under this bill through a joint resolution of disapproval.</p>"
        },
        "title": "United States Reciprocal Trade Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr735.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Reciprocal Trade Act </strong></p><p>This bill expands presidential trade authorities.</p><p>The bill allows the President, in certain circumstances, to (1) negotiate with a foreign country for tariff reductions on exported U.S. goods, or (2) impose additional duties on imported goods. Specifically, the President may take these actions if it is determined that the country (1) when importing a good from the United States, applies a higher rate of duty on that good than the rate imposed by the United States when the good is imported from that country; or (2) similarly imposes other,\u00a0nontariff trade restrictions on that good. This authority\u00a0shall be effective for three years, subject to a three-year renewal.</p><p>The President must terminate a rate of duty increase under this bill if the country no longer applies such higher rates or nontariff trade restrictions, or if the higher rate is no longer in the interest of the United States.</p><p>The bill also requires the President to consult with and notify Congress regarding the intention of the President to increase a rate of duty on imported goods.</p><p>Congress may nullify a rate of duty increase implemented under this bill through a joint resolution of disapproval.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119hr735"
    },
    "title": "United States Reciprocal Trade Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>United States Reciprocal Trade Act </strong></p><p>This bill expands presidential trade authorities.</p><p>The bill allows the President, in certain circumstances, to (1) negotiate with a foreign country for tariff reductions on exported U.S. goods, or (2) impose additional duties on imported goods. Specifically, the President may take these actions if it is determined that the country (1) when importing a good from the United States, applies a higher rate of duty on that good than the rate imposed by the United States when the good is imported from that country; or (2) similarly imposes other,\u00a0nontariff trade restrictions on that good. This authority\u00a0shall be effective for three years, subject to a three-year renewal.</p><p>The President must terminate a rate of duty increase under this bill if the country no longer applies such higher rates or nontariff trade restrictions, or if the higher rate is no longer in the interest of the United States.</p><p>The bill also requires the President to consult with and notify Congress regarding the intention of the President to increase a rate of duty on imported goods.</p><p>Congress may nullify a rate of duty increase implemented under this bill through a joint resolution of disapproval.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119hr735"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr735ih.xml"
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
      "title": "United States Reciprocal Trade Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T08:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States Reciprocal Trade Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T08:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the President to take certain actions relating to reciprocal trade, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T08:03:49Z"
    }
  ]
}
```
