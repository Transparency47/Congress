# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2887?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2887
- Title: Route 66 National Historic Trail Designation Act
- Congress: 119
- Bill type: S
- Bill number: 2887
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2887",
    "number": "2887",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Route 66 National Historic Trail Designation Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
        "item": [
          {
            "date": "2025-09-18T19:33:49Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-18T19:33:49Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MO"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "AZ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2887is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2887\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Cruz (for himself, Ms. Duckworth , Mr. Padilla , Mr. Schmitt , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the National Trails System Act to designate the Route 66 National Historic Trail, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Route 66 National Historic Trail Designation Act .\n#### 2. Designation of the Route 66 National Historic Trail\nSection 5(a) of the National Trails System Act ( 16 U.S.C. 1244(a) ) is amended\u2014\n**(1)**\nby redesignating the second paragraph (31) (relating to the Butterfield Overland National Historic Trail) as paragraph (32); and\n**(2)**\nby adding at the end the following:\n(33) Route 66 National Historic Trail (A) In general The Route 66 National Historic Trail, a trail that includes all the alignments of U.S. Highway 66 in existence between 1926 and 1985, extending along a route of approximately 2,400 miles from Chicago, Illinois, to Santa Monica, California, as generally depicted on the map entitled Route 66 National Historic Trail, Proposed Route , numbered P26/141,279, and dated December 2017. (B) Availability of map The map described in subparagraph (A) shall be on file and available for public inspection at the Department of the Interior. (C) Administration (i) In general The Secretary of the Interior shall administer the Route 66 National Historic Trail in a manner that respects and maintains the idiosyncratic nature of the Route 66 National Historic Trail. (ii) Tribal consultation Consistent with Executive Order 13175 ( 25 U.S.C. 5301 note; relating to consultation and coordination with Indian Tribal governments) and all other applicable Federal law, the Secretary of the Interior shall conduct active, meaningful, and timely consultation with all affected Indian Tribes prior to undertaking an activity with respect to the Route 66 National Historic Trail that would have substantial direct impacts on 1 or more Indian Tribes. (D) Land acquisition The United States shall not acquire for the Route 66 National Historic Trail any land or interest in land that\u2014 (i) is located outside the exterior boundary of any federally managed area without the consent of the owner of the land or interest in land; or (ii) extends more than an average of 1/4 of a mile on either side of the Route 66 National Historic Trail. (E) No buffer zone created (i) In general Nothing in this paragraph, the acquisition of land or an interest in land authorized by this paragraph, or any management plan for the Route 66 National Historic Trail creates or shall be construed to create a buffer zone outside the Route 66 National Historic Trail. (ii) Outside activities The fact that an activity or use on land outside the Route 66 National Historic Trail can be seen, heard, or detected from the Route 66 National Historic Trail, including from any land or interest in land acquired for the Route 66 National Historic Trail subject to the limitations described in subparagraph (D), shall not preclude, limit, control, regulate, or determine the conduct or management of the activity or use. (F) Effect on energy development, production, transportation, or transmission Nothing in this paragraph, the acquisition of land or an interest in land authorized by this paragraph, or any management plan for the Route 66 National Historic Trail shall prohibit, hinder, or disrupt the development, production, transportation, or transmission of energy. (G) No Eminent Domain or Condemnation In carrying out this paragraph, the Secretary of the Interior may not use eminent domain or condemnation. (H) Not a designation of lands in the National Park System Notwithstanding any other provision of law, the designation of the Route 66 National Historic Trail by this paragraph shall not have the effect of designating the Route 66 National Historic Trail or any land on which the Route 66 National Historic Trail is located as lands in the National Park System for purposes of section 28(b)(1) of the Mineral Leasing Act ( 30 U.S.C. 185(b)(1) ). (I) No new authorities or permits (i) No effect on authority To Grant easements or rights-of-way (I) In general Notwithstanding any other provision of law, the designation of the Route 66 National Historic Trail by this paragraph shall not alter or affect the existing authority of any Federal, State, or local agency or official to grant easements or rights-of-way over, under, across, or along any portion of the area designated as the Route 66 National Historic Trail. (II) Authority of heads of Federal agencies to grants easements or rights-of-way Notwithstanding the designation of the Route 66 National Historic Trail by this paragraph, the head of any Federal agency having jurisdiction over any Federal land on which the Route 66 National Historic Trail designated by this paragraph is located (other than land that is considered to be lands in the National Park System for purposes of section 28(b)(1) of the Mineral Leasing Act ( 30 U.S.C. 185(b)(1) ) as a result of a designation under any other law), shall have the authority to grant easements or rights-of-way over, under, across, or along any applicable portion of the Route 66 National Historic Trail in accordance with the laws applicable to the Federal land. (ii) No new permits required Notwithstanding any other provision of law, the designation of the Route 66 National Historic Trail by this paragraph shall not subject the Route 66 National Historic Trail or any land on which the Route 66 National Historic Trail is located to any other Federal laws (including regulations) requiring a Federal permit or authorization that would otherwise be made applicable as a result of the designation of the Route 66 National Historic Trail as a component of the National Trails System. .",
      "versionDate": "2025-09-18",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-01T16:37:58Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2887is.xml"
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
      "title": "Route 66 National Historic Trail Designation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Route 66 National Historic Trail Designation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Trails System Act to designate the Route 66 National Historic Trail, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:19Z"
    }
  ]
}
```
