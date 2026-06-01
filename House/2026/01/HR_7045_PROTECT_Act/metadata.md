# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7045?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7045
- Title: PROTECT Act
- Congress: 119
- Bill type: HR
- Bill number: 7045
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-02-21T09:05:26Z
- Update date including text: 2026-02-21T09:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7045",
    "number": "7045",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000622",
        "district": "1",
        "firstName": "Jimmy",
        "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
        "lastName": "Patronis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PROTECT Act",
    "type": "HR",
    "updateDate": "2026-02-21T09:05:26Z",
    "updateDateIncludingText": "2026-02-21T09:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7045ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7045\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mr. Patronis introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo repeal section 230 of the Communications Act of 1934, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Responsible Online Technology and Ensuring Consumer Trust Act or the PROTECT Act .\n#### 2. Repeal of section 230\n##### (a) In general\nSection 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) is repealed.\n##### (b) Conforming amendments\n**(1) Communications Act of 1934**\nThe Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) is amended\u2014\n**(A)**\nin section 223\u2014\n**(i)**\nin subsection (h)(1)\u2014\n**(I)**\nby striking subparagraph (D); and\n**(II)**\nby redesignating subparagraphs (E) and (F) as subparagraphs (D) and (E), respectively; and\n**(ii)**\nin subsection (i), by striking paragraph (2) and inserting the following:\n(2) The term interactive computer service means any information service, system, or access software provider that provides or enables computer access by multiple users to a computer server, including specifically a service or system that provides access to the internet and such systems operated or services offered by libraries or educational institutions. ; and\n**(B)**\nin section 231(b)(4), by striking or section 230 .\n**(2) Trademark Act of 1946**\nSection 45 of the Act entitled An Act to provide for the registration and protection of trademarks used in commerce, to carry out the provisions of certain international conventions, and for other purposes , approved July 5, 1946 (commonly known as the Trademark Act of 1946 ) ( 15 U.S.C. 1127 ), is amended, in the undesignated provision relating to the term Internet , by striking has the meaning given that term in section 230(f)(1) of the Communications Act of 1934 ( 47 U.S.C. 230(f)(1) ) and inserting means the international computer network of both Federal and non-Federal interoperable packet switched data networks .\n**(3) Title 17, United States Code**\nSection 1401 of title 17, United States Code, is amended by striking subsection (g).\n**(4) Title 18, United States Code**\nPart I of title 18, United States Code, is amended\u2014\n**(A)**\nin section 1462, by striking (as defined in section 230(e)(2) of the Communications Act of 1934) each place it appears and inserting (as defined in section 223(i) of the Communications Act of 1934 ( 47 U.S.C. 223(i) )) ;\n**(B)**\nin section 1465, by striking (as defined in section 230(e)(2) of the Communications Act of 1934) and inserting (as defined in section 223(i) of the Communications Act of 1934 ( 47 U.S.C. 223(i) )) ;\n**(C)**\nin section 2257(h)(2)(B)(v), by striking , except that deletion of a particular communication or material made by another person in a manner consistent with section 230(c) of the Communications Act of 1934 ( 47 U.S.C. 230(c) ) shall not constitute such selection or alteration of the content of the communication ; and\n**(D)**\nin section 2421A\u2014\n**(i)**\nin subsection (a), by striking (as such term is defined in defined in section 230(f) the Communications Act of 1934 ( 47 U.S.C. 230(f) )) and inserting (as such term is defined in section 223(i) of the Communications Act of 1934 ( 47 U.S.C. 223(i) )) ; and\n**(ii)**\nin subsection (b), by striking (as such term is defined in defined in section 230(f) the Communications Act of 1934 ( 47 U.S.C. 230(f) )) and inserting (as such term is defined in section 223(i) of the Communications Act of 1934 ( 47 U.S.C. 223(i) )) .\n**(5) Controlled Substances Act**\nSection 401(h)(3)(A)(iii)(II) of the Controlled Substances Act ( 21 U.S.C. 841(h)(3)(A)(iii)(II) ) is amended by striking , except that deletion of a particular communication or material made by another person in a manner consistent with section 230(c) of the Communications Act of 1934 shall not constitute such selection or alteration of the content of the communication .\n**(6) Webb-Kenyon Act**\nSection 3(b)(1) of the Act entitled An Act divesting intoxicating liquors of their interstate character in certain cases , approved March 1, 1913 (commonly known as the Webb-Kenyon Act ) ( 27 U.S.C. 122b(b)(1) ), is amended by striking (as defined in section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ) and inserting (as defined in section 223(i) of the Communications Act of 1934 ( 47 U.S.C. 223(i) )) .\n**(7) Title 28, United States Code**\nSection 4102 of title 28, United States Code, is amended\u2014\n**(A)**\nby striking subsection (c); and\n**(B)**\nin subsection (e)\u2014\n**(i)**\nby striking construed to and all that follows through affect and inserting construed to affect ; and\n**(ii)**\nby striking defamation; or and all that follows and inserting defamation. .\n**(8) Daniel Anderl Judicial Security and Privacy Act of 2022**\nSection 5933(7) of the Daniel Anderl Judicial Security and Privacy Act of 2022 ( Public Law 117\u2013263 ) is amended by striking section 230 of the Communications Act of 1934 ( 47 U.S.C. 230 ) and inserting section 223(i) of the Communications Act of 1934 ( 47 U.S.C. 223(i) ) .\n**(9) Title 31, United States Code**\nSection 5362(6) of title 31, United States Code, is amended by striking section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ) and inserting section 223(i) of the Communications Act of 1934 ( 47 U.S.C. 223(i) ) .\n**(10) National Telecommunications and Information Administration Organization Act**\nSection 157 of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 941 ) is amended\u2014\n**(A)**\nby striking subsection (e); and\n**(B)**\nby redesignating subsections (f) through (j) as subsections (e) through (i), respectively.\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date of the enactment of this Act.",
      "versionDate": "2026-01-13",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-02-02T14:54:53Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7045ih.xml"
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
      "title": "PROTECT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Responsible Online Technology and Ensuring Consumer Trust Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal section 230 of the Communications Act of 1934, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:18:22Z"
    }
  ]
}
```
