# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2771?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2771
- Title: Forest Legacy Management Flexibility Act
- Congress: 119
- Bill type: HR
- Bill number: 2771
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2026-04-07T08:05:32Z
- Update date including text: 2026-04-07T08:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-09 - IntroReferral: Sponsor introductory remarks on measure. (CR E303)
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-09 - IntroReferral: Sponsor introductory remarks on measure. (CR E303)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2771",
    "number": "2771",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000559",
        "district": "8",
        "firstName": "John",
        "fullName": "Rep. Garamendi, John [D-CA-8]",
        "lastName": "Garamendi",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Forest Legacy Management Flexibility Act",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:32Z",
    "updateDateIncludingText": "2026-04-07T08:05:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E303)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "True",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "OR"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "HI"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "CA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2771ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2771\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Garamendi (for himself, Mr. Calvert , Ms. Bonamici , Mr. Harder of California , Mr. Mullin , and Mr. Costa ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Cooperative Forestry Assistance Act of 1978 to authorize States to approve certain organizations to acquire, hold, and manage conservation easements under the Forest Legacy Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Forest Legacy Management Flexibility Act .\n#### 2. Authority of States to allow qualified organizations to acquire, hold, and manage conservation easements under the Forest Legacy Program\n##### (a) State authorization\nSection 7 of the Cooperative Forestry Assistance Act of 1978 ( 16 U.S.C. 2103c ) is amended\u2014\n**(1)**\nin subsection (l)\u2014\n**(A)**\nin paragraph (2), by striking subsection (m) and inserting subsection (o) ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking the State of Vermont and inserting any State ; and\n**(ii)**\nin subparagraph (B)(ii), in the matter preceding subclause (I), by striking of Vermont and inserting involved ;\n**(2)**\nby redesignating subsection (m) as subsection (o); and\n**(3)**\nby inserting after subsection (l) the following:\n(m) Third-Party conservation easements (1) In general At the request of a State, the Secretary shall authorize the State to approve eligible qualified organizations to acquire, hold, and manage conservation easements to carry out activities under the Forest Legacy Program. (2) Eligibility To be eligible to acquire, hold, and manage a conservation easement under this subsection, a qualified organization shall demonstrate to the Secretary the abilities necessary to acquire, monitor, and enforce interests in forestland\u2014 (A) consistent with the Forest Legacy Program; and (B) in accordance with the applicable assessment of need submitted to the Secretary by the State in which the conservation easement is located. (3) Reversion If the Secretary or a State determines a condition described in paragraph (4) is met with respect to a conservation easement\u2014 (A) all right, title, and interest of the qualified organization in and to the conservation easement shall terminate; and (B) all right, title, and interest in and to the conservation easement shall revert to the State or, if approved by the State, another qualified organization determined eligible by the Secretary under paragraph (2). (4) Conditions for reversion A condition described in this paragraph is, with respect to a conservation easement acquired, held, and managed by a qualified organization, any of the following: (A) The qualified organization is unable to carry out the responsibilities of the qualified organization under the Forest Legacy Program with respect to the conservation easement. (B) The conservation easement has been modified in a way that is inconsistent with the purposes of the Forest Legacy Program or the applicable assessment of need described in paragraph (2)(B). (C) The conservation easement has been conveyed to another person (other than a qualified organization determined eligible by the Secretary under paragraph (2) and approved by the State). (n) Qualified organization defined In this section, the term qualified organization means an organization that\u2014 (1) is a qualified organization, as defined in section 170(h)(3) of the Internal Revenue Code of 1986; (2) is organized for, and at all times since the formation of the organization, has been operated principally for one or more of the conservation purposes described in section 170(h)(4)(A) of such Code; (3) has not been the subject of any criminal or civil enforcement action taken by the Attorney General of the United States or the Commissioner of the Internal Revenue Service pertaining to the charitable donation of conservation easements under such Code; and (4) has been awarded, and at all times thereafter maintained, accredited status by the Land Trust Accreditation Commission, or if such Commission ceases to exist, a successor organization that offers substantially similar accreditation and is approved by the Secretary for purposes of this section. .\n##### (b) Technical corrections\nSection 7 of the Cooperative Forestry Assistance Act of 1978 ( 16 U.S.C. 2103c ) is further amended\u2014\n**(1)**\nin subsection (i), by striking subsection (b) and inserting subsection (c) ;\n**(2)**\nin subsection (l)(3)(B)(i)(II), by inserting and after the semi-colon at the end; and\n**(3)**\nin the header of subsection (o), as redesignated by this section, by striking Appropriation and inserting Authorization of appropriations .",
      "versionDate": "2025-04-09",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-13T15:01:48Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2771ih.xml"
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
      "title": "Forest Legacy Management Flexibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-23T07:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Forest Legacy Management Flexibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T07:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Cooperative Forestry Assistance Act of 1978 to authorize States to approve certain organizations to acquire, hold, and manage conservation easements under the Forest Legacy Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T07:48:21Z"
    }
  ]
}
```
