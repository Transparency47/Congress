# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2394?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2394
- Title: DETERRENCE Act
- Congress: 119
- Bill type: HR
- Bill number: 2394
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2026-04-08T17:56:10Z
- Update date including text: 2026-04-08T17:56:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2394",
    "number": "2394",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000812",
        "district": "2",
        "firstName": "Ann",
        "fullName": "Rep. Wagner, Ann [R-MO-2]",
        "lastName": "Wagner",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "DETERRENCE Act",
    "type": "HR",
    "updateDate": "2026-04-08T17:56:10Z",
    "updateDateIncludingText": "2026-04-08T17:56:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:04:05Z",
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
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2394ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2394\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mrs. Wagner (for herself, Mr. Schneider , and Mr. Moran ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize sentencing enhancements for certain criminal offenses directed by or coordinated with foreign governments.\n#### 1. Short title\nThis Act may be cited as the Deterring External Threats and Ensuring Robust Responses to Egregious and Nefarious Criminal Endeavors Act or the DETERRENCE Act .\n#### 2. Kidnapping\nSection 1201 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (h) as subsection (i);\n**(2)**\nby inserting after subsection (g) the following:\n(h) Sentence enhancements for offenses directed by or coordinated with foreign governments (1) In general The sentence of a person convicted of an offense under subsection (a) may be increased by up to 10 years if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (2) Conspiracy The sentence of a person convicted of conspiring to commit a violation of subsection (a) as part of a conspiracy under the elements specified in subsection (c) may be increased by up to 10 years if\u2014 (A) 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government; and (B) the person convicted of conspiring to commit a violation of subsection (a) knew that 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government. (3) Attempt The sentence of a person convicted of an attempt to violate subsection (a) may be increased by up to 5 years if such attempt was knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. ; and\n**(3)**\nin subsection (i), as so designated, by inserting Definition .\u2014 before As used in this section .\n#### 3. Use of interstate commerce facilities in the commission of murder-for-hire\n##### (a) In general\nSection 1958 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (b) as subsection (c);\n**(2)**\nby inserting after subsection (a) the following:\n(b) Sentence enhancements for offenses directed by or coordinated with foreign governments The sentence of a person convicted of an offense under subsection (a)\u2014 (1) may be increased by up to 5 years, if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government; and (2) may be increased by up to 10 years\u2014 (A) if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government; and (B) personal injury results. ; and\n**(3)**\nin subsection (c), as so redesignated, by inserting Definitions .\u2014 before As used in this section .\n##### (b) Technical and conforming amendments\n**(1)**\nSection 2332b(g)(2) of title 18, United States Code, is amended by striking section 1958(b)(2) and inserting section 1958 .\n**(2)**\nSection 1010A(d) of the Controlled Substances Import and Export Act ( 21 U.S.C. 960a(d) ) is amended by striking section 1958(b)(1) and inserting section 1958 .\n#### 4. Influencing, impeding, or retaliating against a federal official by threatening or injuring a family member\nSection 115(b) of title 18, United States Code, is amended by adding at the end the following:\n(5) The sentence of a person convicted of an offense under subsection (a), if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government\u2014 (A) may be increased by up to 5 years if the offense committed was an assault involving physical contact with the victim of that assault or the intent to commit another felony; (B) may be increased by up to 10 years if\u2014 (i) the offense committed was an assault resulting in bodily injury (including serious bodily injury (as that term is defined in section 1365 of this title)); (ii) the offense involved any conduct that, if the conduct occurred in the special maritime and territorial jurisdiction of the United States, would violate section 2241 or 2242 of this title; or (iii) a dangerous weapon was used during and in relation to the offense; and (C) may be increased by up to 10 years if the offense committed was a murder, attempted murder, or conspiracy to murder. .\n#### 5. Stalking\nSection 2261A of title 18, United States Code, is amended\u2014\n**(1)**\nby striking Whoever\u2014 and inserting (a) In general .\u2014Except as provided in subsection (b), whoever\u2014 ; and\n**(2)**\nby adding at the end the following:\n(b) Enhanced penalties for offenses involving foreign governments The sentence of a person convicted of an offense under paragraph (1) or (2) of subsection (a), if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government\u2014 (1) may be increased by up to 5 years if\u2014 (A) serious bodily injury (including permanent disfigurement or life threatening bodily injury) to the victim results; (B) the offender uses a dangerous weapon during the offense; or (C) the victim of the offense is under the age of 18 years; (2) may be increased by up to 10 years if death of the victim results; and (3) may be increased by up to 30 months in any other case. .\n#### 6. Protection of officers and employees of the United States\nSection 1114 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (b) as subsection (c); and\n**(2)**\nby inserting after subsection (a) the following:\n(b) Sentence enhancements for offenses directed by or coordinated with foreign governments The sentence of a person convicted of an offense under subsection (a) may be increased by up to 10 years if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. .\n#### 7. Presidential and Presidential staff assassination, kidnapping, and assault\nSection 1751 of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (f) through (k) as subsections (g) through (i), respectively; and\n**(2)**\nby inserting after subsection (e) the following:\n(f) (1) The sentence of a person convicted of an offense under subsection (a), (b), or (c) may be increased by up to 10 years if such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (2) The sentence of a person convicted of conspiring to kill or kidnap any individual designated in subsection (a) as part of a conspiracy under the elements specified in subsection (d) may be increased by up to 10 years if\u2014 (A) 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government; and (B) the person convicted of conspiring to kill or kidnap an individual designated in subsection (a) knew that 1 or more of the persons involved in such conspiracy were knowingly acting in coordination with a foreign government or an agent of a foreign government. (3) The sentence of a person convicted of an offense under subsection (e) may be increased by up to 10 years if\u2014 (A) the victim was any person designated in subsection (a)(1); and (B) such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (4) The sentence of a person convicted of an offense under subsection (e) may be increased by up to 10 years if\u2014 (A) the victim was any person designated in subsection (a)(2); and (B) such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. (5) The sentence of a person convicted of an offense under subsection (e) may be increased by up to 10 years if\u2014 (A) (i) the offense involved the use of a dangerous weapon; or (ii) personal injury resulted; and (B) such offense was committed knowingly at the direction of or in coordination with a foreign government or an agent of a foreign government. .",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-06-11",
        "actionTime": "13:35:46",
        "text": "Held at the desk."
      },
      "number": "1136",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DETERRENCE Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-06-23T19:31:40Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-06-23T19:31:40Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-06-23T19:31:40Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-06-23T19:31:40Z"
          },
          {
            "name": "Presidential administrations",
            "updateDate": "2025-06-23T19:31:40Z"
          },
          {
            "name": "Subversive activities",
            "updateDate": "2025-06-23T19:31:40Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-06-23T19:31:40Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-06-23T19:31:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-04-07T14:06:54Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2394ih.xml"
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
      "title": "DETERRENCE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DETERRENCE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deterring External Threats and Ensuring Robust Responses to Egregious and Nefarious Criminal Endeavors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize sentencing enhancements for certain criminal offenses directed by or coordinated with foreign governments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:34Z"
    }
  ]
}
```
