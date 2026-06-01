# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7306?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7306
- Title: CLOSE Act
- Congress: 119
- Bill type: HR
- Bill number: 7306
- Origin chamber: House
- Introduced date: 2026-02-02
- Update date: 2026-02-12T09:06:21Z
- Update date including text: 2026-04-15T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-02: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-02: Introduced in House

## Actions

- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7306",
    "number": "7306",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001222",
        "district": "7",
        "firstName": "Max",
        "fullName": "Rep. Miller, Max L. [R-OH-7]",
        "lastName": "Miller",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "CLOSE Act",
    "type": "HR",
    "updateDate": "2026-02-12T09:06:21Z",
    "updateDateIncludingText": "2026-04-15T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-02",
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
      "actionDate": "2026-02-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-02",
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
          "date": "2026-02-02T14:06:30Z",
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
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "OH"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "OH"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "OH"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7306ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7306\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Mr. Miller of Ohio (for himself, Mr. Turner of Ohio , Mr. Balderson , and Mr. Carey ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the CARES Act to terminate unemployment insurance benefit payments under such Act and to rescind unobligated balances of amounts appropriated for the purpose of such payments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clawing back Lapsed Obligations from State Emergency programs Act or the CLOSE Act .\n#### 2. Rescission of CARES unemployment insurance funds\n##### (a) Pandemic unemployment assistance\n**(1) Termination of assistance payments**\n**(A) In general**\nSection 2102 of the CARES Act ( 15 U.S.C. 9021 ) is amended by adding at the end the following:\n(i) Termination (1) In general Subject to paragraph (2) and notwithstanding any other provision of this section, beginning on the 30th day after the date of enactment of this subsection, this section (except subsections (d)(4) and paragraphs (2) and (3) of subsection (g)) shall have no force or effect. The Secretary may not make payments under subsection (f)(2)(A) after such date. (2) Administrative expenses Notwithstanding paragraph (1), the Secretary may continue to pay to States the amounts described in subsection (f)(2)(B). .\n**(2) Rescission**\n**(A) In general**\nThe unobligated balances of amounts in the extended unemployment compensation account (as established by section 905(a) of the Social Security Act ( 42 U.S.C. 1105(a) ) of the Unemployment Trust Fund (as established by section 904(a) of such Act ( 42 U.S.C. 1104(a) ) that were appropriated pursuant to section 2102(g)(1) of the CARES Act ( 15 U.S.C. 9021(g)(1) ) are hereby rescinded.\n**(B) Effective date**\nSubparagraph (A) shall take effect on the date that is 30 days after the date of enactment of this Act.\n##### (b) Federal Pandemic Unemployment Compensation and Mixed Earner Unemployment Compensation\n**(1) Termination of emergency increase in benefits**\n**(A) In general**\nSection 2104 of the CARES ACT ( 15 U.S.C. 9023 ) is amended by adding at the end the following:\n(j) Termination (1) In general Subject to paragraph (2) and notwithstanding any other provision of this section, beginning on the 30th day after the date of enactment of this subsection, this section (other than subsections (f) and (h) and paragraphs (1)(A)(ii), (1)(B), (2), and (3) of subsection (d)) shall have no force or effect. The Secretary may not make payments under subsection (d)(1)(A)(i) after such date. (2) Administrative expenses Notwithstanding paragraph (1), the Secretary may continue to pay to States the amounts described in subsection (d)(1)(A)(ii). .\n**(2) Prohibition on agreements**\nSection 2104(a) of the CARES Act ( 15 U.S.C. 9023(a) ) is amended by adding at the end the following: No State may enter or reenter an agreement under this section on or after the date of enactment of this sentence.\n**(3) Rescission**\n**(A) In general**\nThe unobligated balances of amounts appropriated under paragraph (3) of subsection (d) of section 2104 of the CARES Act ( 15 U.S.C. 9023 ) for the purposes of carrying out paragraph (1)(A)(i) of such subsection are hereby rescinded.\n**(B) Effective date**\nSubparagraph (A) shall take effect on the date that is 30 days after the date of enactment of this Act.\n##### (c) Pandemic emergency unemployment compensation\n**(1) Repeal**\nSubsections (c) and (d)(1) of section 2107 of the CARES Act ( 15 U.S.C. 9025 ) are hereby repealed.\n**(2) Rescission**\nThe unobligated balances of amounts in the extended unemployment compensation account (as established by section 905(a) of the Social Security Act ( 42 U.S.C. 1105(a) ) of the Unemployment Trust Fund (as established by section 904(a) of such Act ( 42 U.S.C. 1104(a) ) that were appropriated pursuant to section 2107(d)(1) of the CARES Act ( 15 U.S.C. 9025(d)(1) ) are hereby rescinded.\n**(3) Effective date**\nThis subsection and the amendments made by this subsection shall take effect on the date that is 30 days after the date of enactment of this Act.",
      "versionDate": "2026-02-02",
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
        "actionDate": "2026-02-02",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3760",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CLOSE Act",
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
        "name": "Labor and Employment",
        "updateDate": "2026-02-05T18:42:39Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7306ih.xml"
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
      "title": "CLOSE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T13:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLOSE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T13:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clawing back Lapsed Obligations from State Emergency programs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T13:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the CARES Act to terminate unemployment insurance benefit payments under such Act and to rescind unobligated balances of amounts appropriated for the purpose of such payments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T13:03:38Z"
    }
  ]
}
```
