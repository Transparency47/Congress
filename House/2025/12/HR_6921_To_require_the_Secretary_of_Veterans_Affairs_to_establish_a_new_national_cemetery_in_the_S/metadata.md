# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6921?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6921
- Title: Hawai‘i National Cemetery Act
- Congress: 119
- Bill type: HR
- Bill number: 6921
- Origin chamber: House
- Introduced date: 2025-12-23
- Update date: 2026-02-18T09:05:26Z
- Update date including text: 2026-02-18T09:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-23: Introduced in House
- 2025-12-23 - IntroReferral: Introduced in House
- 2025-12-23 - IntroReferral: Introduced in House
- 2025-12-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-12 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-12-23: Introduced in House

## Actions

- 2025-12-23 - IntroReferral: Introduced in House
- 2025-12-23 - IntroReferral: Introduced in House
- 2025-12-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-02-12 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-23",
    "latestAction": {
      "actionDate": "2025-12-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6921",
    "number": "6921",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Hawai\u2018i National Cemetery Act",
    "type": "HR",
    "updateDate": "2026-02-18T09:05:26Z",
    "updateDateIncludingText": "2026-02-18T09:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-23",
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
          "date": "2025-12-23T17:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T19:39:27Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6921ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6921\nIN THE HOUSE OF REPRESENTATIVES\nDecember 23, 2025 Mr. Case (for himself and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to establish a new national cemetery in the State of Hawai\u2019i, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hawai\u2018i National Cemetery Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nVeterans, members of the Armed Forces, spouses, and dependents may be eligible for burial in a national cemetery pursuant to regulations prescribed under section 2402 of title 38, United States Code.\n**(2)**\nAccording to the National Cemetery Administration Strategic Plan and Performance Goals, the Secretary of Veterans Affairs seeks to ensure that 95 percent of veterans live within 75 miles of a national, State, or Tribal veterans cemetery.\n**(3)**\nThe National Cemetery Administration\u2019s Long Range Plan, as detailed in the budget submission of the Department of Veterans Affairs for fiscal year 2026, sets goals that seek to improve burial benefits, including the following:\n**(A)**\nVeterans and eligible family members will have increased access to burial benefits.\n**(B)**\nMore veterans and eligible family members will use such burial and memorial benefits.\n**(C)**\nVeterans will be memorialized through enhanced tributes befitting their service and sacrifice to the Nation.\n**(D)**\nStakeholders will place greater trust in the National Cemetery Administration based on enhanced accountability.\n**(E)**\nStakeholders will be served more efficiently and effectively by internal capacity of the National Cemetery Administration.\n**(4)**\nThe goals described in paragraph (3) do not account for veterans in Hawai\u2018i who prefer to be buried in a national cemetery even if other options exist. Hawai\u2018i\u2019s only national cemetery, the National Memorial Cemetery of the Pacific, has been essentially closed to casketed burials since 1991 and will stop accepting cremated remains by 2036. Should a veteran in Hawai\u2018i prefer an inground burial in a national cemetery, they are forced to select a cemetery at least 2,500 miles away. This distance can create significant financial and logistical burdens compared to veterans in the continental United States, as air travel that is often cost-prohibitive is required for casket transportation and visitation.\n**(5)**\nTo maintain equitable access to burial benefits in a national cemetery for veterans residing in Hawai\u2018i, the Secretary of Veterans Affairs must initiate the construction of a new national cemetery in Hawai\u2018i to supplement the remaining columbarium space at the National Memorial Cemetery of the Pacific. The work should begin immediately, as developing a new national cemetery must pass through six phases and such a cemetery can take more than eight years to construct.\n**(6)**\nWhile Hawai\u2018i is home to many great State Veterans Cemeteries, establishment of a new national cemetery would align with the National Cemetery Administration\u2019s access goals and increase options for veterans and other beneficiaries in the Pacific.\n#### 3. Establishment of new national cemetery in the State of Hawai\u2018i\n##### (a) Establishment\nIn accordance with chapter 24 of title 38, United States Code, and the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), the Secretary of Veterans Affairs shall establish a new national cemetery in the State of Hawai\u2018i.\n##### (b) Site selection\nIn selecting a location for the national cemetery described in subsection (a), the Secretary shall\u2014\n**(1)**\ngive priority to a location that\u2014\n**(A)**\nis near population centers;\n**(B)**\nis accessible by existing modes of transportation; and\n**(C)**\nminimizes environmental impact; and\n**(2)**\nconsult with\u2014\n**(A)**\nthe Governor of Hawai\u2018i;\n**(B)**\nlocal representatives of veterans service organizations; and\n**(C)**\nother entities the Secretary determines appropriate.\n##### (c) Reports\n**(1) Potential sites**\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to the appropriate congressional committees a report identifying sites that the Secretary determines appropriate for the national cemetery described in subsection (a).\n**(2) Progress reports**\nNot later than two years after the date of the enactment of this Act, and annually thereafter until the national cemetery described in subsection (a) is operational, the Secretary shall submit to the appropriate congressional committees a report regarding the establishment of such national cemetery, including progress regarding the following elements:\n**(A)**\nSite selection.\n**(B)**\nEnvironmental impact assessment.\n**(C)**\nLand acquisition.\n**(D)**\nMaster planning and design development.\n**(E)**\nPreparation of construction documents.\n**(F)**\nAward of construction contracts.\n**(G)**\nCompletion of construction.\n**(H)**\nBeginning of operations.\n##### (d) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Veterans' Affairs of the Senate; and\n**(2)**\nthe Committee on Veterans' Affairs of the House of Representatives.",
      "versionDate": "2025-12-23",
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
        "actionDate": "2026-01-12",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3613",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Hawai\u2018i National Cemetery Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-11T13:31:27Z"
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
      "date": "2025-12-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6921ih.xml"
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
      "title": "Hawai\u2018i National Cemetery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T06:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hawai\u2018i National Cemetery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T06:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Veterans Affairs to establish a new national cemetery in the State of Hawai'i, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T06:03:27Z"
    }
  ]
}
```
