# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2315?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2315
- Title: Habitat Enhancement Now Act
- Congress: 119
- Bill type: S
- Bill number: 2315
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2025-12-18T12:03:19Z
- Update date including text: 2025-12-18T12:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2315",
    "number": "2315",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Habitat Enhancement Now Act",
    "type": "S",
    "updateDate": "2025-12-18T12:03:19Z",
    "updateDateIncludingText": "2025-12-18T12:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T23:54:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2315is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2315\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mrs. Hyde-Smith introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo establish grant programs to sustain populations of species of migratory waterfowl through the deployment of tools and practices that complement habitat conservation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Habitat Enhancement Now Act .\n#### 2. Grant programs to sustain populations of species of migratory waterfowl\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nthe maintenance of healthy populations of migratory birds in North America is largely dependent on the protection, restoration, and management of wetland ecosystems and other habitats, as identified in the Implementation Plans of Joint Ventures authorized under the North American Waterfowl Management Plan;\n**(2)**\nduck populations in North America are being threatened by the loss in the quantity and quality of breeding habitat, which leads to declining nest success;\n**(3)**\nlow nest success has been widely documented to be the key annual driver in duck populations;\n**(4)**\nadditional tools can be employed to increase nest success to complement the private, State, and Federal habitat conservation programs and efforts in order to sustain healthy waterfowl populations;\n**(5)**\nrelatively modest investments in management can make meaningful impacts towards supplementing waterfowl production in areas where waterfowl production outcomes have not been fully met;\n**(6)**\nnumerous studies have made it clear that nesting structures, in particular hen houses , are the most efficient and cost-effective tool for increasing nest success; and\n**(7)**\nproviding incentives to private landowners to establish nesting cover, create or restore brood ponds, and provide brood water is a priority to enhance production of mallards, gadwalls, and other breeding ducks in California.\n##### (b) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State, local, or Tribal government;\n**(B)**\na nonprofit organization; and\n**(C)**\nan individual.\n**(2) Hen house**\nThe term hen house means a type of cylindrical nest structure installed on a post in a prairie pothole.\n**(3) Prairie pothole**\nThe term prairie pothole means a depressional wetland, including a freshwater marsh, that provides vital habitat to species of nesting waterfowl and other species.\n**(4) Prairie pothole region**\nThe term prairie pothole region means the primary nesting grounds of the majority of North American ducks.\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior.\n##### (c) Grant programs\n**(1) Hen house grant program**\n**(A) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a competitive grant program to award amounts to eligible entities to strategically place, build, and maintain hen houses in the prairie pothole region for the purpose of improving the nesting success rates of populations of species of migratory waterfowl.\n**(B) Applications**\nTo be eligible to receive a grant under this paragraph, an eligible entity shall submit to the Secretary an application in such form, at such time, and containing such information as the Secretary determines appropriate.\n**(2) Breeding habitat grant program**\n**(A) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a competitive grant program to award amounts to eligible entities to develop breeding habitat for species of migratory waterfowl within California for the purpose of enhancing the breeding success rates of populations of species of migratory waterfowl, including by\u2014\n**(i)**\nestablishing nesting cover;\n**(ii)**\ncreating brood ponds; and\n**(iii)**\nproviding incentives to willing landowners to carry out the activities described in this subparagraph on land under the control of those landowners within California.\n**(B) Applications**\nTo be eligible to receive a grant under this paragraph, an eligible entity shall submit to the Secretary an application in such form, at such time, and containing such information as the Secretary determines appropriate.\n##### (d) Funding\nFor each of fiscal years 2026 through 2030, of the amounts appropriated or otherwise made available to the Department of the Interior\u2014Office of the Secretary\u2014Departmental Operations account for each such fiscal year\u2014\n**(1)**\n$3,500,000 shall be made available to carry out subsection (c)(1); and\n**(2)**\n$3,500,000 shall be made available to carry out subsection (c)(2).",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-07-22",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "4591",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Habitat Enhancement Now Act",
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
        "name": "Environmental Protection",
        "updateDate": "2025-09-16T13:24:00Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2315is.xml"
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
      "title": "Habitat Enhancement Now Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Habitat Enhancement Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish grant programs to sustain populations of species of migratory waterfowl through the deployment of tools and practices that complement habitat conservation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:30Z"
    }
  ]
}
```
