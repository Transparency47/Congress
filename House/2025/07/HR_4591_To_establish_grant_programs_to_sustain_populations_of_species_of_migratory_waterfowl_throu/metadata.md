# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4591?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4591
- Title: Habitat Enhancement Now Act
- Congress: 119
- Bill type: HR
- Bill number: 4591
- Origin chamber: House
- Introduced date: 2025-07-22
- Update date: 2025-12-05T22:53:05Z
- Update date including text: 2025-12-05T22:53:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-07-22: Introduced in House

## Actions

- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4591",
    "number": "4591",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "F000470",
        "district": "7",
        "firstName": "Michelle",
        "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
        "lastName": "Fischbach",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Habitat Enhancement Now Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:53:05Z",
    "updateDateIncludingText": "2025-12-05T22:53:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T14:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "CA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CA"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4591ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4591\nIN THE HOUSE OF REPRESENTATIVES\nJuly 22, 2025 Mrs. Fischbach (for herself, Mr. LaMalfa , and Mr. Thompson of California ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo establish grant programs to sustain populations of species of migratory waterfowl through the deployment of tools and practices that complement habitat conservation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Habitat Enhancement Now Act .\n#### 2. Grant programs to sustain populations of species of migratory waterfowl\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe maintenance of healthy populations of migratory birds in North America is largely dependent on the protection, restoration, and management of wetland ecosystems and other habitats, as identified in the Implementation Plans of Joint Ventures authorized under the North American Waterfowl Management Plan;\n**(2)**\nduck populations in North America are being threatened by the loss in the quantity and quality of breeding habitat, which leads to declining nest success;\n**(3)**\nlow nest success has been widely documented to be the key annual driver in duck populations;\n**(4)**\nadditional tools can be employed to increase nest success to complement the private, State, and Federal habitat conservation programs and efforts in order to sustain healthy waterfowl populations;\n**(5)**\nrelatively modest investments in management can make meaningful impacts towards supplementing waterfowl production in areas where waterfowl production outcomes have not been fully met;\n**(6)**\nnumerous studies have made it clear that nesting structures, in particular hen houses , are the most efficient and cost-effective tool for increasing nest success; and\n**(7)**\nproviding incentives to private landowners to establish nesting cover, create or restore brood ponds, and provide brood water is a priority to enhance production of mallards, gadwalls, and other breeding ducks in California.\n##### (b) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State, local, or Tribal government;\n**(B)**\na nonprofit organization; and\n**(C)**\nan individual.\n**(2) Hen house**\nThe term hen house means a type of cylindrical nest structure installed on a post in a prairie pothole.\n**(3) Prairie pothole**\nThe term prairie pothole means a depressional wetland, including a freshwater marsh, that provides vital habitat to species of nesting waterfowl and other species.\n**(4) Prairie pothole region**\nThe term prairie pothole region means the primary nesting grounds of the majority of North American ducks.\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior.\n##### (c) Grant programs\n**(1) Hen house grant program**\n**(A) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a competitive grant program to award amounts to eligible entities to strategically place, build, and maintain hen houses in the prairie pothole region for the purpose of improving the nesting success rates of populations of species of migratory waterfowl.\n**(B) Applications**\nTo be eligible to receive a grant under this paragraph, an eligible entity shall submit to the Secretary an application in such form, at such time, and containing such information as the Secretary determines appropriate.\n**(2) Breeding habitat grant program**\n**(A) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a competitive grant program to award amounts to eligible entities to develop breeding habitat for species of migratory waterfowl within California for the purpose of enhancing the breeding success rates of populations of species of migratory waterfowl, including by\u2014\n**(i)**\nestablishing nesting cover;\n**(ii)**\ncreating brood ponds; and\n**(iii)**\nproviding incentives to willing landowners to carry out the activities described in this subparagraph on land under the control of those landowners within California.\n**(B) Applications**\nTo be eligible to receive a grant under this paragraph, an eligible entity shall submit to the Secretary an application in such form, at such time, and containing such information as the Secretary determines appropriate.\n##### (d) Funding\nFor each of fiscal years 2026 through 2030, of the amounts appropriated or otherwise made available to the Department of the Interior\u2014Office of the Secretary\u2014Departmental Operations account for each such fiscal year\u2014\n**(1)**\n$3,500,000 shall be made available to carry out subsection (c)(1); and\n**(2)**\n$3,500,000 shall be made available to carry out subsection (c)(2).",
      "versionDate": "2025-07-22",
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
        "actionDate": "2025-07-16",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "2315",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Habitat Enhancement Now Act",
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
        "name": "Environmental Protection",
        "updateDate": "2025-09-16T13:50:20Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4591ih.xml"
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
      "title": "Habitat Enhancement Now Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Habitat Enhancement Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish grant programs to sustain populations of species of migratory waterfowl through the deployment of tools and practices that complement habitat conservation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T05:03:33Z"
    }
  ]
}
```
