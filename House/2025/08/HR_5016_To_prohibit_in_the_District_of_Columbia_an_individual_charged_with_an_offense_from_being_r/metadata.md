# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5016?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5016
- Title: Keep Offenders Off Our Streets Act.
- Congress: 119
- Bill type: HR
- Bill number: 5016
- Origin chamber: House
- Introduced date: 2025-08-22
- Update date: 2025-09-26T15:31:17Z
- Update date including text: 2025-09-26T15:31:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-22: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-08-22: Introduced in House

## Actions

- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-22",
    "latestAction": {
      "actionDate": "2025-08-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5016",
    "number": "5016",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Keep Offenders Off Our Streets Act.",
    "type": "HR",
    "updateDate": "2025-09-26T15:31:17Z",
    "updateDateIncludingText": "2025-09-26T15:31:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-22",
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
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-22",
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
          "date": "2025-08-22T13:01:45Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "LA"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "TX"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "MD"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "IN"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5016ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5016\nIN THE HOUSE OF REPRESENTATIVES\nAugust 22, 2025 Mr. Biggs of Arizona (for himself, Mr. Higgins of Louisiana , Mr. Nehls , and Mr. Harris of Maryland ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit in the District of Columbia an individual charged with an offense from being released pending trial without executing an secured appearance bond.\n#### 1. Short title\nThis Act may be cited as the Keep Offenders Off Our Streets Act. .\n#### 2. Prohibition in district of columbia on release of individual charged with offense pending trial without executing a secured appearance bond\n##### (a) In general\nThe Council of the District of Columbia may not enact, and the Mayor of the District of Columbia may not enforce, any act, resolution, regulation, or other requirement which permits an individual charged with an offense in the District of Columbia who appears before a judicial officer, as defined in section 23\u20131331(1), District of Columbia Official Code, to be released, pending trial, without such person executing a bail bond with solvent sureties in whatever amount is reasonably necessary to assure the appearance of the individual as required.\n##### (b) Conforming amendments\n**(1) Repeal of release on personal recognizance**\nSection 23\u20131321 District of Columbia 11 Official Code, is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking subsection (1); and\n**(ii)**\nredesignating subsections (2), (3), and (4) as subsections (1), (2), and (3), respectively;\n**(B)**\nby striking subsection (b);\n**(C)**\nby redesignating subsections (c), (d), and (e) as subsections (b), (c), and (d), respectively; and\n**(D)**\nin subsection (b), as so redesignated\u2014\n**(i)**\nin subsection (1), by striking everything before the judicial officer ;\n**(ii)**\nin subsection (A), by striking and after the semicolon;\n**(iii)**\nredesignating subsection (B) as subsection (C);\n**(iv)**\nafter subsection (A), insert the following:\n(B) Execution of a bail bond with solvent sureties in whatever amount is reasonably necessary to assure the appearance of the person as required; and ; and\n**(v)**\nin subsection (C), as so redesignated, strike subsection (xii), and redesignate subsection (xiv) as subsection (xiii).\n**(2) Inclusion of prohibition in home rule act**\nSection 602(a) of the District of Columbia Home Rule Act (sec. 1\u2013206.02(a), D.C. Official Code) is amended\u2014\n**(A)**\nin paragraph (9), by striking office; or and inserting a office; ;\n**(B)**\nin paragraph (10), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following new paragraph:\n(11) enact any act, resolution, regulation or other requirement which permits a person charged with an offense in the District of Columbia to be released, pending trial, without such person executing an bail bond with solvent sureties in whatever amount is reasonably necessary to assure the appearance of the person as required. .\n##### (c) Applicability\nThis Act, and the amendments made by this Act, shall apply with respect to an individual charged with an offense in the District of Columbia who appears before a judicial officer, as defined in section 23\u2013 1331(1), District of Columbia Official Code, before, on, or after the date of the enactment of this Act.\n##### (d) Severability\nIf, for any reason, any provision of this Act, or an amendment made by this Act, is held invalid, such invalidity shall not affect the validity of the remaining provisions of this Act.",
      "versionDate": "2025-08-22",
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
        "updateDate": "2025-09-26T15:31:17Z"
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
      "date": "2025-08-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5016ih.xml"
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
      "title": "Keep Offenders Off Our Streets Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-26T03:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep Offenders Off Our Streets Act.",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T03:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit in the District of Columbia an individual charged with an offense from being released pending trial without executing an secured appearance bond.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-26T03:48:18Z"
    }
  ]
}
```
