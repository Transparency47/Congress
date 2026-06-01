# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7167?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7167
- Title: Make It Count Act
- Congress: 119
- Bill type: HR
- Bill number: 7167
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-04-16T17:06:15Z
- Update date including text: 2026-04-16T17:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-21 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-21 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7167",
    "number": "7167",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Make It Count Act",
    "type": "HR",
    "updateDate": "2026-04-16T17:06:15Z",
    "updateDateIncludingText": "2026-04-16T17:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-21T15:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7167ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7167\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Mr. Barrett introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require a citizenship question on the decennial census, to require reporting on certain census statistics, to modify apportionment of Representatives to be based on United States citizens instead of all persons, to prohibit States from carrying out more than one Congressional redistricting after a decennial census and apportionment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Make It Count Act .\n#### 2. Citizenship status on decennial census\n##### (a) In general\nSection 141 of title 13, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (g) as subsection (h); and\n**(2)**\nby inserting after subsection (f) the following:\n(g) (1) In conducting the 2030 decennial census and each decennial census thereafter, the Secretary shall include in any questionnaire distributed or otherwise used for the purpose of determining the total population by States a checkbox or other similar option for the respondent to indicate, for the respondent and for each of the members of the household of the respondent, whether that individual is\u2014 (A) a citizen of the United States; (B) a national of the United States but not a citizen of the United States; (C) an alien lawfully residing in the United States; or (D) an alien unlawfully residing in the United States. (2) Not later than 120 days after completion of a decennial census of the population under subsection (a), the Secretary shall make publicly available the number of persons per State, disaggregated by each of the 4 categories described in subparagraphs (A) through (D) of paragraph (1), as tabulated in accordance with this section. .\n#### 3. Exclusion of noncitizens from number of persons used to determine apportionment of representatives and number of electoral votes\n##### (a) Exclusion\nSection 22(a) of the Act entitled An Act to provide for the fifteenth and subsequent decennial censuses and to provide for an apportionment of Representatives in Congress , approved June 18, 1929 ( 2 U.S.C. 2a(a) ), is amended by inserting after not taxed the following: and individuals who are not citizens of the United States .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply with respect to the apportionment of Representatives carried out pursuant to the decennial census conducted during 2030 and any succeeding decennial census.\n#### 4. Limit on congressional redistricting after an apportionment\n##### (a) In general\nThe Act entitled An Act for the relief of Doctor Ricardo Vallejo Samala and to provide for congressional redistricting , approved December 14, 1967 ( 2 U.S.C. 2c ), is amended by adding at the end the following: A State which has been redistricted in the manner provided by law after an apportionment under section 22(a) of the Act entitled An Act to provide for the fifteenth and subsequent decennial censuses and to provide for an apportionment of Representatives in Congress , approved June 18, 1929 ( 2 U.S.C. 2a ), may not be redistricted again until after the next apportionment of Representatives under such section, unless a court requires the State to conduct such subsequent redistricting to comply with the Constitution or to enforce the Voting Rights Act of 1965 ( 42 U.S.C. 1973 et seq. ). .\n##### (b) No effect on elections for State and local office\nNothing in this section or in any amendment made by this section may be construed to affect the manner in which a State carries out elections for State or local office, including the process by which a State establishes the districts used in such elections.\n##### (c) Effective date\nThis section and the amendment made by this section shall apply with respect to any Congressional redistricting which occurs after the November 2024 election.\n#### 5. Severability clause\nIf any provision of this Act or amendment made by this Act, or the application thereof to any person or circumstance, is held to be unconstitutional, the remainder of the provisions of this Act and amendments made by this Act, and the application of the provision or amendment to any other person or circumstance, shall not be affected.",
      "versionDate": "2026-01-21",
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
        "actionDate": "2025-12-02",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 20 - 19."
      },
      "number": "151",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Equal Representation Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-29",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2205",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Equal Representation Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-11T13:45:58Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7167ih.xml"
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
      "title": "Make It Count Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Make It Count Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a citizenship question on the decennial census, to require reporting on certain census statistics, to modify apportionment of Representatives to be based on United States citizens instead of all persons, to prohibit States from carrying out more than one Congressional redistricting after a decennial census and apportionment, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T04:48:18Z"
    }
  ]
}
```
