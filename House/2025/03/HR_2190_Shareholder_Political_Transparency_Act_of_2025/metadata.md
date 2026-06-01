# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2190?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2190
- Title: Shareholder Political Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2190
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-05-09T16:06:05Z
- Update date including text: 2025-05-09T16:06:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2190",
    "number": "2190",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Shareholder Political Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-09T16:06:05Z",
    "updateDateIncludingText": "2025-05-09T16:06:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:08:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "OH"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CT"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2190ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2190\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Foster (for himself, Ms. Vel\u00e1zquez , Mrs. Beatty , Ms. Schakowsky , Mr. Casten , Mr. Garc\u00eda of Illinois , and Mr. Himes ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Exchange Act of 1934 to require reporting of certain expenditures for political activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shareholder Political Transparency Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\ncorporations make significant political contributions and expenditures that directly or indirectly influence the election of candidates and support or oppose political causes;\n**(2)**\ndecisions to use corporate funds for political contributions and expenditures are usually made by corporate boards and executives, rather than shareholders;\n**(3)**\ncorporations, acting through boards and executives, are obligated to conduct business for the best interests of their owners, the shareholders;\n**(4)**\nhistorically, shareholders have not had a way to know, or to influence, the political activities of corporations they own;\n**(5)**\nshareholders and the public have a right to know how corporate managers are spending company funds to make political contributions and expenditures benefitting candidates, political parties, and political causes; and\n**(6)**\ncorporations should be accountable to shareholders in making political contributions or expenditures affecting Federal governance and public policy.\n#### 3. Reporting requirements\nSection 13 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78m ) is amended by adding at the end the following:\n(t) Reporting requirements relating to certain political expenditures (1) Definitions In this subsection: (A) Expenditure for political activities The term expenditure for political activities \u2014 (i) means\u2014 (I) an independent expenditure (as defined in section 301(17) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101(17) )); (II) an electioneering communication (as defined in section 304(f)(3) of that Act ( 52 U.S.C. 30104(f)(3) )) and any other public communication (as defined in section 301(22) of that Act ( 52 U.S.C. 30101(22) )) that would be an electioneering communication if it were a broadcast, cable, or satellite communication; or (III) dues or other payments to trade associations or organizations described in section 501(c) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of that Code that are, or could reasonably be anticipated to be, used or transferred to another association or organization for the purposes described in subclause (I) or (II); and (ii) does not include\u2014 (I) direct lobbying efforts through registered lobbyists employed or hired by the issuer; (II) communications by an issuer to its shareholders and executive or administrative personnel and their families; or (III) the establishment and administration of contributions to a separate segregated fund to be utilized for political purposes by a corporation. (B) Issuer The term issuer does not include an investment company registered under section 8 of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20138 ). (2) Quarterly reports (A) Reports required Not later than 180 days after the date of enactment of this subsection, the Commission shall amend the reporting rules under this section to require each issuer with a class of equity securities registered under section 12 of this title to submit to the Commission and the shareholders of the issuer a quarterly report containing\u2014 (i) a description of any expenditure for political activities made during the preceding quarter; (ii) the date of each expenditure for political activities; (iii) the amount of each expenditure for political activities; (iv) if the expenditure for political activities was made in support of or in opposition to a candidate, the name of the candidate and the office sought by, and the political party affiliation of, the candidate; and (v) the name or identity of trade associations or organizations described in section 501(c) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such Code which receive dues or other payments as described in paragraph (1)(A)(i)(III). (B) Public availability The Commission shall ensure that the quarterly reports required under this paragraph are publicly available through the Internet website of the Commission and through the EDGAR system in a manner that is searchable, sortable, and downloadable, consistent with the requirements under section 24. (3) Annual reports Not later than 180 days after the date of enactment of this subsection, the Commission shall, by rule, require each issuer to include in the annual report of the issuer to shareholders\u2014 (A) a summary of each expenditure for political activities made during the preceding year in excess of $10,000, and each expenditure for political activities for a particular election if the total amount of such expenditures for that election is in excess of $10,000; (B) a description of the specific nature of any expenditure for political activities the issuer intends to make for the forthcoming fiscal year, to the extent the specific nature is known to the issuer; and (C) the total amount of expenditures for political activities intended to be made by the issuer for the forthcoming fiscal year. (4) Reports to Congress (A) Assessment and report The Commission shall\u2014 (i) conduct an annual assessment of the compliance of issuers with this subsection; and (ii) submit to Congress an annual report containing the results of such assessment. (B) Government Accountability Office The Comptroller General of the United States shall periodically evaluate and report to Congress on the effectiveness of the oversight by the Commission of the reporting and disclosure requirements under this subsection. .",
      "versionDate": "2025-03-18",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-09T16:06:05Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2190ih.xml"
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
      "title": "Shareholder Political Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shareholder Political Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Securities Exchange Act of 1934 to require reporting of certain expenditures for political activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:43Z"
    }
  ]
}
```
