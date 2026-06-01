# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6306?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6306
- Title: AI Fraud Deterrence Act
- Congress: 119
- Bill type: HR
- Bill number: 6306
- Origin chamber: House
- Introduced date: 2025-11-25
- Update date: 2025-12-11T15:20:59Z
- Update date including text: 2025-12-11T15:20:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-25: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-11-25: Introduced in House

## Actions

- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-25",
    "latestAction": {
      "actionDate": "2025-11-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6306",
    "number": "6306",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000582",
        "district": "36",
        "firstName": "Ted",
        "fullName": "Rep. Lieu, Ted [D-CA-36]",
        "lastName": "Lieu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "AI Fraud Deterrence Act",
    "type": "HR",
    "updateDate": "2025-12-11T15:20:59Z",
    "updateDateIncludingText": "2025-12-11T15:20:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-25",
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
      "actionDate": "2025-11-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-25",
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
          "date": "2025-11-25T16:01:10Z",
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
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6306ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6306\nIN THE HOUSE OF REPRESENTATIVES\nNovember 25, 2025 Mr. Lieu (for himself and Mr. Dunn of Florida ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo increase penalties for the commission of financial crimes using artificial intelligence.\n#### 1. Short title\nThis Act may be cited as the AI Fraud Deterrence Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nScammers are using AI to impersonate senior U.S. government officials.\n**(2)**\nIn May 2025, hackers breached the personal cellphone of White House Chief of Staff Susie Wiles and used AI to impersonate her voice in calls and messages to senators, governors, business leaders, and other high-level contacts.\n**(3)**\nIn July 2025, AI was used to impersonate Secretary of State Marco Rubio\u2019s voice in calls to three foreign ministers, a Member of Congress, and a Governor, with the apparent aim of obtaining sensitive information and access to accounts.\n#### 3. Financial crimes and artificial intelligence\n##### (a) Mail fraud\nSection 1341 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking $1,000,000 and inserting $2,000,000 ; and\n**(2)**\nby inserting after the period at the end the following: If the violation is committed with the assistance of artificial intelligence, such person shall be fined not more than $1,000,000 or imprisoned not more than 20 years, or both. .\n##### (b) Wire fraud\nSection 1343 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking $1,000,000 and inserting $2,000,000 ; and\n**(2)**\nby inserting after the period at the end the following: If the violation is committed with the assistance of artificial intelligence, such person shall be fined not more than $1,000,000 or imprisoned not more than 20 years, or both. .\n##### (c) Bank fraud\nSection 1344 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking Whoever knowingly and inserting the following:\n(a) In general Whoever knowingly ; and\n**(2)**\nby adding at the end the following:\n(b) Artificial intelligence Whoever commits subsection (a) with the assistance of artificial intelligence shall be fined not more than $2,000,000 or imprisoned not more than 30 years, or both. .\n##### (d) Artificial intelligence defined\n**(1) In general**\nSection 1346 of title 18, United States Code, is amended\u2014\n**(A)**\nby amending the section heading to read as follows: Definitions ;\n**(B)**\nby striking chapter, the term and inserting the following:\nchapter\u2014 (1) the term ;\n**(C)**\nby striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(2) the term artificial intelligence has the meaning given such term in section 5002 of the National Artificial Intelligence Initiative Act of 2020. .\n**(2) Clerical amendment**\nThe table of sections for chapter 63 of title 18, United States Code, is amended by striking the item relating to section 1346 and inserting the following:\n1346. Definitions. .\n##### (e) Money laundering\nSection 1956 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the continuation text following paragraph (1)(B)(ii), by inserting after or both the following: , or, in the case that such violation is committed with the assistance of artificial intelligence, shall be fined not more than $1,000,000 or thrice the value of the monetary instrument or funds involved in the transaction, whichever is greater, or imprisoned for not more than 20 years, or both ;\n**(B)**\nin the continuation text following paragraph (2)(B)(ii), by inserting after or both the following: , or, in the case that such violation is committed with the assistance of artificial intelligence, shall be fined not more than $1,000,000 or thrice the value of the monetary instrument or funds involved in the transportation, transmission, or transfer, whichever is greater, or imprisoned for not more than 20 years, or both ; and\n**(C)**\nin the continuation text following paragraph (3)(C), by inserting after or both the following: , or, in the case that such violation is committed with the assistance of artificial intelligence, shall be fined under this title, or imprisoned for not more than 20 years, or both ; and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (8), by striking and at the end;\n**(B)**\nin paragraph (9), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(10) the term artificial intelligence has the meaning given such term in section 5002 of the National Artificial Intelligence Initiative Act of 2020. .\n#### 4. Ai impersonation of Federal officials\nSection 912 of title 18, United States Code, is amended\u2014\n**(1)**\nby inserting after the period at the end the following: If the violation is committed with the assistance of artificial intelligence, such person shall be fined not more than $1,000,000 or imprisoned not more than 3 years, or both. ;\n**(2)**\nby striking Whoever and inserting the following:\n(a) In general Whoever ;\n**(3)**\nby inserting after falsely assumes or pretends to be an officer or employee the following: , including with the use of artificial intelligence, ; and\n**(4)**\nby adding at the end the following:\n(b) Rule of construction Nothing in this section shall be construed to limit legitimate uses of artificial intelligence in satire, parody, or expressive conduct protected under the First Amendment, provided such content includes clear disclosure that it is not authentic and is not intended as such. (c) Definition In this section, the term artificial intelligence has the meaning given such term in section 5002 of the National Artificial Intelligence Initiative Act of 2020. .",
      "versionDate": "2025-11-25",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-11T15:20:58Z"
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
      "date": "2025-11-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6306ih.xml"
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
      "title": "AI Fraud Deterrence Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T11:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AI Fraud Deterrence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-10T11:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase penalties for the commission of financial crimes using artificial intelligence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-10T11:03:25Z"
    }
  ]
}
```
