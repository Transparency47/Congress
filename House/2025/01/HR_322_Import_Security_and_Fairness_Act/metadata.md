# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/322?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/322
- Title: Import Security and Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 322
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-02-26T09:06:24Z
- Update date including text: 2025-02-26T09:06:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/322",
    "number": "322",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001201",
        "district": "3",
        "firstName": "Thomas",
        "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
        "lastName": "Suozzi",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Import Security and Fairness Act",
    "type": "HR",
    "updateDate": "2025-02-26T09:06:24Z",
    "updateDateIncludingText": "2025-02-26T09:06:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:34:40Z",
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
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr322ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 322\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Suozzi (for himself and Mr. Dunn of Florida ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Tariff Act of 1930 relating to de minimis treatment under that Act.\n#### 1. Short title\nThis Act may be cited as the \u201c Import Security and Fairness Act \u201d.\n#### 2. Additional exceptions to exemptions for de minimis treatment under the Tariff Act of 1930\nSection 321 of the Tariff Act of 1930 ( 19 U.S.C. 1321 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking \u201c(a) The Secretary\u201d and inserting \u201c(a) In general .\u2014The Secretary\u201d;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (C), by striking \u201c$800\u201d and inserting \u201cexcept as provided in subsection (b)(1), $800\u201d; and\n**(ii)**\nin the matter following subparagraph (C), as so amended, by striking \u201csubdivision (2)\u201d each place it appears and inserting \u201cparagraph\u201d; and\n**(2)**\nby striking \u201c(b) The Secretary\u201d and inserting the following:\n(b) Exceptions (1) In general An article may not be admitted free of duty or tax under the authority provided by subsection (a)(2)(C) if the country of origin of such article, or the country from which such article is shipped, is\u2014 (A) a nonmarket economy country (as such term is defined in section 771(18)); and (B) a country included in the priority watch list (as such term is defined in section 182(g)(3) of the Trade Act of 1974 ( 19 U.S.C. 2242(g)(3) )). (2) Other exceptions The Secretary .\n#### 3. Additional administrative provisions relating to de minimis treatment under the Tariff Act of 1930\n##### (a) Administrative exemptions\nSection 321 of the Tariff Act of 1930 ( 19 U.S.C. 1321 ), as amended by section 2, is further amended by adding at the end the following:\n(c) Submission of documentation and information (1) In general For any articles that may qualify for an administrative exemption pursuant to subsection (a)(2), the Secretary of the Treasury shall, not later than 180 days after the date of the enactment of the Import Security and Fairness Act, prescribe regulations to require the submission, transmission, or otherwise making available of such documentation or information to U.S. Customs and Border Protection as the Secretary determines is reasonably necessary for U.S. Customs and Border Protection to determine the eligibility of such articles to qualify for such exemption. (2) Matters to be included The regulations prescribed under paragraph (1)\u2014 (A) shall require that documentation or information with respect to an article described in that paragraph include, at a minimum\u2014 (i) a description of the article; (ii) the appropriate classification of the article under the Harmonized Tariff Schedule of the United States; (iii) the country of origin of the article; (iv) the country from which the article is shipped; (v) the identity of the shipper; (vi) the identity of the importer; and (vii) the transaction value of the article in the United States; and (B) may provide that such documentation or information include other documentation or information regarding the offer for sale or purchase, or the subsequent sale, purchase, transportation, importation or warehousing of an article described in paragraph (1), including such documentation or information relating to the offering of the article for sale or purchase in the United States through a commercial or marketing platform, including an electronic commercial or marketing platform. (3) Veracity of documentation and information (A) In general The regulations prescribed pursuant to paragraph (1) shall provide that\u2014 (i) the documentation or information described in that paragraph is true and correct to the best of the knowledge and belief of the party submitting, transmitting, or otherwise making available such documentation or information, subject to any penalties authorized by law; or (ii) if such party is not able to reasonably verify whether such documentation or information is true and correct to the best of the knowledge and belief of the party, such documentation or information may be submitted, transmitted, or otherwise made available on the basis of what the party reasonably believes to be true and correct. (B) Use for any lawful purpose Such documentation or information may be used by U.S. Customs and Border Protection for any lawful purpose. (4) Civil penalties Any person who violates the regulations prescribed pursuant to paragraph (1) is liable for a civil penalty of $5,000 for the first violation, and $10,000 for each subsequent violation. A penalty imposed under this paragraph is in addition to any other penalty provided by law. (d) Importations involving suspended or debarred persons The Secretary of the Treasury is authorized to prescribe regulations to authorize exceptions to any administrative exemption pursuant to subsection (a) for any articles the importation of which is caused or otherwise facilitated by any person suspended or debarred from doing business with the Federal Government at the time of the importation. .\n##### (b) Examination of merchandise\nSection 499(c) of the Tariff Act of 1930 ( 19 U.S.C. 1499(c) ) is amended\u2014\n**(1)**\nby striking the Customs Service each place it appears and inserting U.S. Customs and Border Protection ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the first sentence, by striking The Customs Service and inserting the following:\n(A) In general U.S. Customs and Border Protection ;\n**(B)**\nin the second sentence\u2014\n**(i)**\nby striking The and inserting the following:\n(B) Information to be included The ; and\n**(ii)**\nby redesignating the subsequent subparagraphs (A), (B), (C), (D), and (E) as clauses (i), (ii), (iii), (iv), and (v), respectively, and moving such clauses, as redesignated, 2 ems to the right; and\n**(C)**\nby adding at the end the following:\n(C) Additional requirements relating to merchandise that may qualify for certain administrative exemptions (i) In general In a case in which U.S. Customs and Border Protection has made a decision to detain merchandise that may qualify for an administrative exemption pursuant to section 321(a)(2)(C), U.S. Customs and Border Protection shall issue such notice to each party that U.S. Customs and Border Protections determines may have an interest in the detained merchandise, based on information reasonably available to U.S. Customs and Border Protection, in such form and manner as the Secretary of the Treasury shall by regulation prescribe. (ii) Voluntary abandonment of merchandise In the case of merchandise described in clause (i), such notice shall also advise each such interested party that, in lieu of supplying information to U.S. Customs and Border Protection in accordance with subparagraph (B)(v), the interested parties may voluntarily abandon the merchandise. (iii) Abandonment or export due to lack of response If U.S. Customs and Border Protection does not receive a response from each interested party in merchandise described in clause (i) within 30 days of the date on which such notice is issued to the interested parties, the merchandise may\u2014 (I) be denied entry and be permitted to be exported, with the importer responsible for paying all expenses of exportation; or (II) be deemed to be abandoned, in which case title to such merchandise shall be vested in the United States and the merchandise shall be disposed of in accordance with law. .\n#### 4. Effective date\nThe amendments made by this Act shall apply with respect to articles entered, or withdrawn from warehouse for consumption, on or after the 180th day after the date of the enactment of this Act.",
      "versionDate": "2025-01-09",
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
            "updateDate": "2025-02-24T19:33:05Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-02-24T19:33:18Z"
          },
          {
            "name": "Customs enforcement",
            "updateDate": "2025-02-24T19:32:53Z"
          },
          {
            "name": "Department of the Treasury",
            "updateDate": "2025-02-24T19:33:26Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-24T19:33:13Z"
          },
          {
            "name": "Tariffs",
            "updateDate": "2025-02-24T19:32:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-02-19T17:55:58Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr322ih.xml"
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
      "title": "Import Security and Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Import Security and Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T09:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Tariff Act of 1930 relating to de minimis treatment under that Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T09:18:24Z"
    }
  ]
}
```
