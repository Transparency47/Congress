# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4080?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4080
- Title: GUARD Act
- Congress: 119
- Bill type: HR
- Bill number: 4080
- Origin chamber: House
- Introduced date: 2025-06-23
- Update date: 2025-07-15T10:33:58Z
- Update date including text: 2025-07-15T10:33:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-23: Introduced in House

## Actions

- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4080",
    "number": "4080",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001101",
        "district": "10",
        "firstName": "Pat",
        "fullName": "Rep. Harrigan, Pat [R-NC-10]",
        "lastName": "Harrigan",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "GUARD Act",
    "type": "HR",
    "updateDate": "2025-07-15T10:33:58Z",
    "updateDateIncludingText": "2025-07-15T10:33:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
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
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T16:01:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4080ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4080\nIN THE HOUSE OF REPRESENTATIVES\nJune 23, 2025 Mr. Harrigan introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to authorize the use of National Guard forces for immigration enforcement purposes, to establish criminal penalties for assaulting immigration enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guarding U.S. Authority for Removal and Detention Act or the GUARD Act .\n#### 2. Amendment to the posse comitatus act\nSection 1385 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking Whoever and inserting (a) Whoever ; and\n**(2)**\nby adding at the end the following new subsection:\n(b) Exceptions Subsection (a) shall not apply to the use of members of the National Guard\u2014 (1) performing State duty under orders issued by the Governor of such State; or (2) performing duty under title 10 or 32, if such members are used exclusively for\u2014 (A) the enforcement of the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act (8 U.S.C.1101)), including the apprehension or detention of aliens unlawfully present in the United States, and the execution of orders of removal issued under the immigration laws; or (B) border security operations. .\n#### 3. Assaulting immigration enforcement personnel\n##### (a) Assault on Federal Immigration Officers or State Law Enforcement Assisting Immigration Operations\nChapter 7 of title 18, United States Code, is amended by adding at the end the following:\n119A. Assault on immigration enforcement officers (a) Whoever knowingly assaults, resists, opposes, impedes, intimidates, or interferes with\u2014 (1) any officer or employee of U.S. Immigration and Customs Enforcement, U.S. Customs and Border Protection, or any other Federal immigration enforcement agency; or (2) any State or local law enforcement officer acting under Federal authority or in active assistance of Federal immigration enforcement operations in the performance of their official duties, or on account of the performance of such duties, shall be fined under this title and imprisoned not less than 5 years and not more than 20 years. (b) If bodily injury results from the acts committed in violation of subsection (a), the term of imprisonment shall be not less than 10 years and not more than 30 years. (c) If death results from the acts committed in violation of subsection (a), the offender shall be subject to imprisonment for life or the death penalty. .\n##### (b) Clerical amendment\nThe table of sections for chapter 7 of title 18, United States Code, is amended by inserting after the item relating to section 119 the following:\n119A. Assault on immigration enforcement officers. .",
      "versionDate": "2025-06-23",
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
        "updateDate": "2025-07-15T10:33:57Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4080ih.xml"
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
      "title": "GUARD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GUARD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guarding U.S. Authority for Removal and Detention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to authorize the use of National Guard forces for immigration enforcement purposes, to establish criminal penalties for assaulting immigration enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:28Z"
    }
  ]
}
```
