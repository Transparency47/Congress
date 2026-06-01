# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1560?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1560
- Title: Secure U.S. Leadership in Space Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1560
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2025-12-05T21:58:39Z
- Update date including text: 2025-12-05T21:58:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1560",
    "number": "1560",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Secure U.S. Leadership in Space Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:58:39Z",
    "updateDateIncludingText": "2025-12-05T21:58:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T16:00:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1560is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1560\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mrs. Moody (for herself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to treat spaceports like airports for purposes of exempt facility bond rules.\n#### 1. Short title\nThis Act may be cited as the Secure U.S. Leadership in Space Act of 2025 .\n#### 2. Spaceports are treated like airports under exempt facility bond rules\n##### (a) In general\nSection 142(a)(1) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) airports and spaceports, .\n##### (b) Treatment of ground leases\nSection 142(b)(1) of such Code is amended by adding at the end the following new subparagraph:\n(C) Special rule for spaceport ground leases For purposes of subparagraph (A), spaceport property located on land leased by a governmental unit from the United States shall not fail to be treated as owned by a governmental unit if the requirements of this paragraph are met by the lease and any subleases of the property. .\n##### (c) Definition of spaceport\nSection 142 of such Code is amended by adding at the end the following new subsection:\n(p) Spaceport (1) In general For purposes of subsection (a)(1), the term spaceport means any facility located at or in close proximity to a launch site or reentry site used for\u2014 (A) manufacturing, assembling, or repairing spacecraft, space cargo, other facilities described in this paragraph, or any component of the foregoing, (B) flight control operations, (C) providing launch services and reentry services, or (D) transferring crew, spaceflight participants, or space cargo to or from spacecraft. (2) Additional terms For purposes of paragraph (1)\u2014 (A) Space cargo The term space cargo includes satellites, scientific experiments, other property transported into space, and any other type of payload, whether or not such property returns from space. (B) Spacecraft The term spacecraft means a launch vehicle or a reentry vehicle. (C) Other terms The terms launch , launch site , crew , space flight participant , launch services , launch vehicle , payload , reenter , reentry services , reentry site , a reentry vehicle shall have the respective meanings given to such terms by section 50902 of title 51, United States Code (as in effect on the date of enactment of this subsection). (3) Public use requirement Notwithstanding any other provision of law, a facility shall not be required to be available for use by the general public to be treated as a spaceport for purposes of this section. (4) Manufacturing facilities and industrial parks allowed With respect to spaceports, subsection (c)(2)(E) shall not apply to spaceport property described in paragraph (1)(A). .\n##### (d) Exception from federally guaranteed bond prohibition\nSection 149(b)(3) of such Code is amended by adding at the end the following new subparagraph:\n(F) Exception for spaceports A bond shall not be treated as federally guaranteed merely because of the payment of rent, user fees, or other charges by the United States (or any agency or instrumentality thereof) in exchange for the use of the spaceport by the United States (or any agency or instrumentality thereof). .\n##### (e) Exclusion from State ceiling\nSection 146(g) of such Code is amended by striking and at the end of paragraph (5), by striking the period and inserting , and at the end of paragraph (6), and by inserting after paragraph (6) the following new paragraph:\n(7) any exempt facility bond issued as part of an issue 95 percent or more of the net proceeds of which are to be used to provide a spaceport (as defined in section 142). .\n##### (f) Conforming amendment\nThe heading for section 142(c) of such Code is amended by inserting Spaceports, after Airports, .\n##### (g) Effective date\nThe amendments made by this section shall apply to obligations issued after the date of the enactment of this Act.",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-05-01",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "3142",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Secure U.S. Leadership in Space Act of 2025",
      "type": "HR"
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
        "name": "Taxation",
        "updateDate": "2025-06-04T15:21:35Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1560is.xml"
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
      "title": "Secure U.S. Leadership in Space Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Secure U.S. Leadership in Space Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to treat spaceports like airports for purposes of exempt facility bond rules.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:40Z"
    }
  ]
}
```
