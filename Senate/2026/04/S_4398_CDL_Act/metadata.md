# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4398?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4398
- Title: CDL Act
- Congress: 119
- Bill type: S
- Bill number: 4398
- Origin chamber: Senate
- Introduced date: 2026-04-27
- Update date: 2026-05-19T21:57:40Z
- Update date including text: 2026-05-19T21:57:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in Senate
- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-04-27: Introduced in Senate

## Actions

- 2026-04-27 - IntroReferral: Introduced in Senate
- 2026-04-27 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4398",
    "number": "4398",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "CDL Act",
    "type": "S",
    "updateDate": "2026-05-19T21:57:40Z",
    "updateDateIncludingText": "2026-05-19T21:57:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T22:18:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "WY"
    },
    {
      "bioguideId": "A000383",
      "firstName": "Alan",
      "fullName": "Sen. Armstrong, Alan [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Armstrong",
      "middleName": "Stuart",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4398is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4398\nIN THE SENATE OF THE UNITED STATES\nApril 27, 2026 Mr. Lankford (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require new State-issued driver's licenses and identification cards to indicate whether or not the holder is a United States citizen in order to be acceptable for Federal recognition and to establish minimum requirements for Federal recognition of State-issued commercial driver's licenses and non-domicile commercial driver's licenses.\n#### 1. Short titles\nThis Act may be cited as the Citizenship Documented License Act or the CDL Act .\n#### 2. Requirement for Federally-recognized driver's licenses and identification cards to indicate whether the holder is a United States citizen\n##### (a) In general\nSection 202(b) of the REAL ID Act of 2005 (division B of Public Law 109\u201313 ; 49 U.S.C. 30301 note) is amended by adding at the end the following:\n(10) Indication that the person is a United States citizen or is not a United States citizen. .\n##### (b) Effective date; applicability\nThe requirement described in section 202(b)(10) of the REAL ID Act of 2005, as added by subsection (a), shall only apply to State-issued driver's licenses and identification cards issued on or after the date that is 60 days after the date of the enactment of this Act.\n#### 3. Minimum requirements for commercial driver's licenses and non-domicile commercial driver's licenses to warrant Federal recognition\nTitle II of the REAL ID Act of 2005 (division B of Public Law 109\u201313 ; 49 U.S.C. 30301 note) is amended by inserting after section 202 the following:\n202A. Minimum requirements for commercial driver's licenses and non-domicile commercial driver's licenses to warrant Federal recognition (a) In general Subject to subsection (b), a Federal agency may not accept, for any official purpose, a commercial driver's license issued by a State to any person unless the State, before issuing such a license\u2014 (1) required the person to present, and verified the validity of, the information described in section 202(c)(1); and (2) has verified the person is\u2014 (A) a national of the United States (as defined in section 101(a)(22) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(22) )); (B) an alien lawfully admitted for permanent residence (as defined in section 101(a)(20) of such Act ( 8 U.S.C. 1101(a)(20) )); or (C) a nonimmigrant described in subparagraph (E)(ii), (H)(ii)(a), or (H)(ii)(b) of section 101(a)(15) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15) ) who is in possession of a valid, unexpired nonimmigrant visa issued to such nonimmigrant. (b) Exceptions The provisions relating to minimum issuance standards set forth in clauses (v) through (ix) of subparagraph (B) and subparagraph (C) of section 202(c)(2) shall not apply to the issuance of a commercial driver's license under subsection (a). .",
      "versionDate": "2026-04-27",
      "versionType": "Introduced in Senate"
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
        "name": "Immigration",
        "updateDate": "2026-05-19T21:57:39Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4398is.xml"
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
      "title": "CDL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CDL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Citizenship Documented License Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require new State-issued driver's licenses and identification cards to indicate whether or not the holder is a United States citizen in order to be acceptable for Federal recognition and to establish minimum requirements for Federal recognition of State-issued commercial driver's licenses and non-domicile commercial driver's licenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:34Z"
    }
  ]
}
```
