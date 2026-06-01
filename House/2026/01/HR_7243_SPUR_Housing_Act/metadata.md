# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7243?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7243
- Title: SPUR Housing Act
- Congress: 119
- Bill type: HR
- Bill number: 7243
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-02-12T15:52:48Z
- Update date including text: 2026-02-12T15:52:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7243",
    "number": "7243",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001326",
        "district": "5",
        "firstName": "Janelle",
        "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
        "lastName": "Bynum",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "SPUR Housing Act",
    "type": "HR",
    "updateDate": "2026-02-12T15:52:48Z",
    "updateDateIncludingText": "2026-02-12T15:52:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:30:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7243ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7243\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Ms. Bynum (for herself and Mr. Pappas ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of Housing and Urban Development to establish a grant program to provide amounts to developers to offset the State and local taxes associated with the building of housing developments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Projects to Unleash Residential Housing Act or the SPUR Housing Act .\n#### 2. Grant program\n##### (a) In general\nThe Secretary of Housing and Urban Development shall, not later than 90 days after the date of the enactment of this Act establish a grant program to provide amounts to developers that such developers may use to offset costs such developer accrues associated with\u2014\n**(1)**\nState and local taxes associated with the building of housing developments; and\n**(2)**\nimpact fees imposed by States and units of local government in association with the building of housing developments.\n##### (b) Application\nTo be eligible to receive amounts under this section an developer shall submit an application to the Secretary at such time and in such manner as the Secretary may reasonably require.\n##### (c) Additional eligibility requirements\nTo be eligible to receive amounts under this section, an developer shall have\u2014\n**(1)**\nall approvals required from the State government and each unit of local government with jurisdiction over the area in which developer intends to build a housing development; and\n**(2)**\ncommitments from the State government and each unit of local government with jurisdiction over the area in which developer intends to build a housing development that the State government and each unit of local government shall reduce the property taxes associated with the housing developments to be built by the developer by not less than 50 percent.\n##### (d) Selection\nWhen selecting developers to receive amounts under this section the Secretary shall prioritize giving grants to developers who are building housing developments that, as determined by the Secretary\u2014\n**(1)**\nwill increase the amount of affordable housing;\n**(2)**\nare feasible;\n**(3)**\nare able to begin building within 1 year of the date on which the eligible developer submitted an application;\n**(4)**\nare to be located in a priority housing area, as identified by the Secretary using housing market indicators and the severe housing cost burden data from the American Community Survey conducted by the Bureau of the Census;\n**(5)**\nthat will offer affordable or mixed-income housing units;\n**(6)**\nare transit-oriented developments or located near employment hubs;\n**(7)**\nwill utilize infill sites within urban growth boundaries;\n**(8)**\nwill target workforce housing needs;\n**(9)**\nwill include senior-friendly units and accessible units;\n**(10)**\nwill employ adaptive reuse or rehabilitation of existing structures; and\n**(11)**\nwill include supportive housing elements for vulnerable populations.\n##### (e) Amount of grant\nThe Secretary shall provide, each year, to each developer to whom the Secretary selects to receive a grant under this section, a grant in an amount equal to the lesser of\u2014\n**(1)**\n50 percent of the total amount of the taxes and impact fees to be imposed on the developer by the State government and each unit of local government with jurisdiction over the area in which developer intends to build a housing development in association with the building such housing development; or\n**(2)**\n$150,000.\n##### (f) Term of grant\nThe Secretary shall provide grants to each developer selected to receive a grant under this section for 5 years, unless such developer does not have the commitments from the State government and units of local government that are required under subsection (c) for each of those 5 years.\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary $300,000,000 in each of fiscal years 2027 through fiscal 2031 to carry out this section.\n##### (h) Definitions\nIn this section:\n**(1) Impact fee**\nThe term impact fee means a charge imposed by a local government on a new housing development to help pay for public infrastructure and services needed because of such housing development.\n**(2) Developer**\nThe term developer means a person that plans, finances, and oversees the creation or redevelopment of real estate or infrastructure projects, from initial concept through completion.\n**(3) Housing development**\nThe term housing development means a project involving the building or rehabilitation of 5 or more or more residential housing units and includes mixed-use housing developments.\n**(4) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.",
      "versionDate": "2026-01-27",
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
        "name": "Housing and Community Development",
        "updateDate": "2026-02-12T15:52:48Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7243ih.xml"
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
      "title": "SPUR Housing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SPUR Housing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Projects to Unleash Residential Housing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Housing and Urban Development to establish a grant program to provide amounts to developers to offset the State and local taxes associated with the building of housing developments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:37Z"
    }
  ]
}
```
