# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/776?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/776
- Title: UNITED Act
- Congress: 119
- Bill type: S
- Bill number: 776
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-12-05T22:01:19Z
- Update date including text: 2025-12-05T22:01:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/776",
    "number": "776",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "UNITED Act",
    "type": "S",
    "updateDate": "2025-12-05T22:01:19Z",
    "updateDateIncludingText": "2025-12-05T22:01:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
        "item": {
          "date": "2025-02-27T17:06:49Z",
          "name": "Referred To"
        }
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s776is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 776\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Coons (for himself and Mr. Moran ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide the President with authority to enter into a comprehensive trade agreement with the United Kingdom, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Undertaking Negotiations on Investment and Trade for Economic Dynamism Act or the UNITED Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe United States should pursue more open trade and investment relationships with its allies to strengthen the economy of the United States, improve the standard of living of the people of the United States, and advance the strategic interests of the United States;\n**(2)**\nagreements to reduce or eliminate barriers to trade and investment between the United States and its allies will foster mutually beneficial economic relationships that advance the economic interests of workers, farmers, ranchers, and businesses of all sizes in the United States;\n**(3)**\nthe shared values and long history of the special relationship between the United States and the United Kingdom present a unique opportunity to deepen the mutually beneficial economic and strategic relationship between those countries and further expand prosperity for the citizens of those countries;\n**(4)**\na high-standard, comprehensive trade agreement between the United States and the United Kingdom would help strengthen that relationship, improve the economic prospects of people in both countries, increase the resilience of critical supply chains, and create export opportunities for businesses of all sizes;\n**(5)**\nthe efforts of the United States-United Kingdom Trade and Investment Working Group and the bilateral negotiations initiated by President Donald J. Trump have laid groundwork toward a comprehensive trade agreement;\n**(6)**\nthe United States-United Kingdom Dialogue on the Future of Atlantic Trade, initiated by President Joseph R. Biden, along with the signing of the document entitled Atlantic Declaration: A Framework for a Twenty-First Century U.S.-U.K. Economic Partnership , continued efforts to improve economic cooperation between the United States and United Kingdom;\n**(7)**\nthe robust labor and environmental protections in the United Kingdom reduce the risk of regulatory arbitrage that undercuts workers and businesses in the United States;\n**(8)**\nCongress passed the USMCA with overwhelming bipartisan support, setting high standards in North America with respect to labor rights, the environment, intellectual property, non-market practices, and services, and those standards should inform future negotiations;\n**(9)**\ntrade agreements with foreign trading partners that share the values and ambition of the United States offer an opportunity to build on the USMCA and set high international standards across many important policy areas;\n**(10)**\nany trade negotiations between the United States and the United Kingdom must honor the agreement between the Government of Ireland and the Government of the United Kingdom signed on April 10, 1998 (commonly known as the Good Friday Agreement ), and any trade agreement between those countries must advance peace, stability, and prosperity in Ireland and Northern Ireland;\n**(11)**\nthe United Kingdom, like many key trading partners of the United States, is actively negotiating for expanded access to foreign markets, and the United States must likewise seek to advance its access to foreign markets to ensure that businesses, consumers, farmers, ranchers, and workers in the United States are not left behind; and\n**(12)**\nto effectively pursue comprehensive trade negotiations with the United Kingdom for purposes of a trade agreement between the United States and the United Kingdom, Congress must grant new negotiating authority to the President, which should\u2014\n**(A)**\nenable the swift negotiation and passage through Congress of such an agreement; and\n**(B)**\nbe narrowly tailored to provide clear direction to the executive branch of the United States Government.\n#### 3. Definitions\nIn this Act:\n**(1) USMCA**\nThe term USMCA means the Agreement between the United States of America, the United Mexican States, and Canada, which is\u2014\n**(A)**\nattached as an Annex to the Protocol Replacing the North American Free Trade Agreement with the Agreement between the United States of America, the United Mexican States, and Canada, done at Buenos Aires on November 30, 2018, as amended by the Protocol of Amendment to the Agreement Between the United States of America, the United Mexican States, and Canada, done at Mexico City on December 10, 2019; and\n**(B)**\napproved by Congress under section 101(a)(1) of the United States\u2013Mexico\u2013Canada Agreement Implementation Act ( 19 U.S.C. 4511(a) ).\n**(2) United Kingdom**\nThe term United Kingdom means the United Kingdom of Great Britain and Northern Ireland.\n#### 4. Negotiating and trade agreements authority for comprehensive agreement with the United Kingdom\n##### (a) Initiation of negotiations\nNot later than 180 days after the date of the enactment of this Act, in order to enhance the economic well-being of the United States, the President shall seek to initiate negotiations with the United Kingdom regarding tariff and nontariff barriers affecting any industry, product, or service sector.\n##### (b) Authority for comprehensive trade agreement with the United Kingdom\n**(1) In general**\nTo strengthen the economic competitiveness of the United States, the President may enter into a comprehensive trade agreement with the United Kingdom regarding tariff and nontariff barriers affecting trade between the United States and United Kingdom.\n**(2) Termination of authority**\nThe authority under paragraph (1) terminates on March 1, 2029.\n##### (c) Modifications permitted\n**(1) In general**\nSubject to paragraph (2), the President may proclaim such modification or continuance of any existing duty, continuance of existing duty-free or excise treatment, or such additional duties as the President determines to be required or appropriate to carry out an agreement entered into under subsection (b).\n**(2) Limitations**\n**(A) Modifications or additions to agreement**\nSubstantial modifications to, or substantial additional provisions of, an agreement entered into after March 1, 2029, are not covered by the authority under paragraph (1).\n**(B) Amount of duty modification**\nNo proclamation may be made under paragraph (1) that\u2014\n**(i)**\nreduces any rate of duty (other than a rate of duty that does not exceed 5 percent ad valorem on the date of the enactment of this Act) to a rate of duty that is less than 50 percent of the rate of such duty that applies on such date of enactment;\n**(ii)**\nreduces the rate of duty below that applicable under the Uruguay Round Agreements (as defined in section 2(7) of the Uruguay Round Agreements Act ( 19 U.S.C. 3501 )) or a successor agreement, on any import sensitive agricultural product; or\n**(iii)**\nincreases any rate of duty above the rate that applied on the date of the enactment of this Act.\n##### (d) Consultation with and notification to Congress\nTo ensure the alignment of the trade policy priorities of Congress with the content of any agreement under this section, the President shall consult with Congress before and throughout negotiations initiated under subsection (a) and shall notify Congress of the intention of the President to enter into an agreement under subsection (b) or to make a proclamation under subsection (c).\n##### (e) Bills qualifying for trade authorities procedures\n**(1) Implementing bills**\n**(A) In general**\nThe provisions of section 151 of the Trade Act of 1974 ( 19 U.S.C. 2191 ) apply to a bill of either House of Congress that contains provisions described in subparagraph (B) to the same extent as such section 151 applies to implementing bills under that section. A bill to which this paragraph applies shall hereafter in this section be referred to as an implementing bill .\n**(B) Provisions specified**\nThe provisions described in this subparagraph are\u2014\n**(i)**\na provision approving a trade agreement entered into under this section and approving the statement of administrative action, if any, proposed to implement such trade agreement; and\n**(ii)**\nif changes in existing laws or new statutory authority are required to implement such trade agreement, only such provisions as are strictly necessary or appropriate to implement such trade agreement, either repealing or amending existing laws or providing new statutory authority.\n**(2) Deadline for submission of bill**\nThe procedures under paragraph (1) apply to implementing bills submitted with respect to a trade agreement entered into under this section before March 1, 2029.\n##### (f) Limitation on waiver, suspension, or termination\nAn agreement entered into under this section shall not be waived, suspended, or terminated, in whole or in part, with respect to the United States without the express approval by Congress of such termination.\n##### (g) Relationship to Bipartisan Congressional Trade Priorities and Accountability Act of 2015\nAn agreement under this section shall not enter into force with respect to the United States and an implementing bill shall not qualify for trade authorities procedures under subsection (e), including an agreement that does not require changes to United States law or an implementing bill in connection therewith, unless the following requirements under the Bipartisan Congressional Trade Priorities and Accountability Act of 2015 ( 19 U.S.C. 4201 et seq. ) are carried out with respect to that agreement or implementing bill to the same extent as would be required of an agreement entered into under section 103(b) of that Act ( 19 U.S.C. 4202(b) ), notwithstanding the expiration of authority to enter into an agreement under such section 103(b):\n**(1)**\nThe trade negotiating objectives under section 102 of that Act ( 19 U.S.C. 4201 ).\n**(2)**\nThe congressional oversight and consultation requirements under section 104 of that Act ( 19 U.S.C. 4203 ).\n**(3)**\nThe notification, consultation, and reporting requirements under section 105 of that Act ( 19 U.S.C. 4204 ).\n**(4)**\nThe implementation procedures under section 106 of that Act ( 19 U.S.C. 4205 ).\n**(5)**\nThe provisions related to sovereignty under section 108 of that Act ( 19 U.S.C. 4207 ).",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1743",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "UNITED Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-09-02T19:18:12Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-09-02T19:18:12Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-09-02T19:18:12Z"
          },
          {
            "name": "Free trade and trade barriers",
            "updateDate": "2025-09-02T19:18:12Z"
          },
          {
            "name": "Tariffs",
            "updateDate": "2025-09-02T19:18:12Z"
          },
          {
            "name": "Trade agreements and negotiations",
            "updateDate": "2025-09-02T19:18:12Z"
          },
          {
            "name": "United Kingdom",
            "updateDate": "2025-09-02T19:18:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-07-03T23:14:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119s776",
          "measure-number": "776",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2025-07-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s776v00",
            "update-date": "2025-07-09"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Undertaking Negotiations on Investment and Trade for Economic Dynamism Act or the UNITED Act</strong></p><p>This bill grants certain authorities to the President for entering into a comprehensive trade agreement between the United States and the United Kingdom (UK).</p><p>Specifically, the bill directs the President to seek to initiate negotiations with the UK regarding tariff and nontariff barriers affecting any industry, product, or service sector.</p><p>The bill authorizes the President to enter into a comprehensive trade agreement with the UK, with such authority expiring on March 1, 2029. Further, the President may proclaim a modification or continuance of any existing duty or a continuance of existing excise or duty-free treatment to carry out an agreement, with certain limitations.</p><p>The bill also requires the President to consult with and notify Congress regarding the intention of the President to enter into an agreement or make a proclamation.</p>"
        },
        "title": "UNITED Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s776.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Undertaking Negotiations on Investment and Trade for Economic Dynamism Act or the UNITED Act</strong></p><p>This bill grants certain authorities to the President for entering into a comprehensive trade agreement between the United States and the United Kingdom (UK).</p><p>Specifically, the bill directs the President to seek to initiate negotiations with the UK regarding tariff and nontariff barriers affecting any industry, product, or service sector.</p><p>The bill authorizes the President to enter into a comprehensive trade agreement with the UK, with such authority expiring on March 1, 2029. Further, the President may proclaim a modification or continuance of any existing duty or a continuance of existing excise or duty-free treatment to carry out an agreement, with certain limitations.</p><p>The bill also requires the President to consult with and notify Congress regarding the intention of the President to enter into an agreement or make a proclamation.</p>",
      "updateDate": "2025-07-09",
      "versionCode": "id119s776"
    },
    "title": "UNITED Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Undertaking Negotiations on Investment and Trade for Economic Dynamism Act or the UNITED Act</strong></p><p>This bill grants certain authorities to the President for entering into a comprehensive trade agreement between the United States and the United Kingdom (UK).</p><p>Specifically, the bill directs the President to seek to initiate negotiations with the UK regarding tariff and nontariff barriers affecting any industry, product, or service sector.</p><p>The bill authorizes the President to enter into a comprehensive trade agreement with the UK, with such authority expiring on March 1, 2029. Further, the President may proclaim a modification or continuance of any existing duty or a continuance of existing excise or duty-free treatment to carry out an agreement, with certain limitations.</p><p>The bill also requires the President to consult with and notify Congress regarding the intention of the President to enter into an agreement or make a proclamation.</p>",
      "updateDate": "2025-07-09",
      "versionCode": "id119s776"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s776is.xml"
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
      "title": "UNITED Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "UNITED Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Undertaking Negotiations on Investment and Trade for Economic Dynamism Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide the President with authority to enter into a comprehensive trade agreement with the United Kingdom, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:05Z"
    }
  ]
}
```
