# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5470?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5470
- Title: Route 66 National Historic Trail Designation Act
- Congress: 119
- Bill type: HR
- Bill number: 5470
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-05-30T08:05:36Z
- Update date including text: 2026-05-30T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Natural Resources.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5470",
    "number": "5470",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Route 66 National Historic Trail Designation Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:36Z",
    "updateDateIncludingText": "2026-05-30T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:05:45Z",
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
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NM"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "IL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "KS"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "KS"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "IL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "IL"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "OK"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "MO"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "IL"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "AZ"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "AZ"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5470ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5470\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. LaHood (for himself and Ms. Leger Fernandez ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the National Trails System Act to designate the Route 66 National Historic Trail, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Route 66 National Historic Trail Designation Act .\n#### 2. Designation of Route 66 National Historic Trail\nSection 5(a) of the National Trails System Act ( 16 U.S.C. 1244(a) ) is amended\u2014\n**(1)**\nby redesignating the second paragraph (31) (relating to Butterfield Overland National Historic Trail) as paragraph (32); and\n**(2)**\nby adding at the end the following:\n(33) Route 66 national historic trail (A) In general The Route 66 National Historic Trail, a trail that includes all the alignments of U.S. Highway 66 in existence between 1926 and 1985, extending along a route of approximately 2,400 miles from Chicago, Illinois, to Santa Monica, California, as generally depicted on the map entitled Route 66 National Historic Trail, Proposed Route , numbered P26/141,279, and dated December 2017. (B) Availability of map The map described in subparagraph (A) shall be on file and available for public inspection in the appropriate offices of the National Park Service, Department of the Interior. (C) Administration (i) In general The Route 66 National Historic Trail shall be administered by the Secretary of the Interior, acting through the Director of the National Park Service. Such administration shall be conducted in a manner that respects and maintains the idiosyncratic nature of the Route 66 National Historic Trail. (ii) Tribal consultation Consistent with Executive Order 13175 ( 25 U.S.C. 5301 note; relating to consultation and coordination with Indian Tribal Governments) and all other applicable Federal law, the Secretary of the Interior shall conduct active, meaningful, and timely consultation with all affected Indian Tribes prior to undertaking an activity with respect to the Route 66 National Historic Trail that would have substantial direct impacts on 1 or more Indian Tribes. (D) Land acquisition The United States may not acquire for the Route 66 National Historic Trail any land or interest in land\u2014 (i) outside the exterior boundary of any federally managed area without the consent of the owner of the land or interest in land; or (ii) that extends more than an average of one-quarter of a mile on either side of the trail. (E) No buffer zone created Nothing in this Act, the acquisition of the land or an interest in land authorized by this Act, or the management plan for the Route 66 National Historic Trail shall be construed to create buffer zones outside of the Trail. That activities or uses can be seen, heard, or detected from the acquired land shall not preclude, limit, control, regulate, or determine the conduct or management of activities or uses outside of the trail. (F) Energy Nothing in this Act, the acquisition of land or an interest in land authorized by this Act, or the management plan for the Route 66 National Historic Trail shall prohibit, hinder, or disrupt the current or future development, production, transportation, or transmission of energy, including the construction or maintenance of pipelines, renewable energy projects, or other infrastructure for the development, production, transportation, or transmission of energy. (G) Eminent domain or condemnation In carrying out this Act, the Secretary of the Interior may not use eminent domain or condemnation. (H) Not a designation of lands in the national park system Notwithstanding any other provision of law, the designation of the Route 66 National Historic Trail by this paragraph shall not have the effect of designating the Route 66 National Historic Trail or any land on which the Route 66 National Historic Trail is located as lands in the National Park System for purposes of section 28(b)(1) of the Mineral Leasing Act ( 30 U.S.C. 185(b)(1) ). (I) No new authorities or permit (i) No effect on authority to grant easements or rights-of-way (I) In general Notwithstanding any other provision of law, the designation of the Route 66 National Historic Trail by this paragraph shall not alter or affect the existing authority of any Federal, State, or local agency or official to grant easements or rights-of-way over, under, across, or along any portion of the area designated as the Route 66 National Historic Trail. (II) Authority of heads of federal agencies to grants easements or rights-of-way Notwithstanding the designation of the Route 66 National Historic Trail by this paragraph, the head of any Federal agency having jurisdiction over any Federal land on which the Route 66 National Historic Trail designated by this paragraph is located (other than land that is considered to be lands in the National Park System for purposes of section 28(b)(1) of the Mineral Leasing Act ( 30 U.S.C. 185(b)(1) ) as a result of a designation under any other law), shall have the authority to grant easements or rights-of-way over, under, across, or along any applicable portion of the Route 66 National Historic Trail in accordance with the laws applicable to the Federal land. (ii) No new permits required Notwithstanding any other provision of law, the designation of the Route 66 National Historic Trail by this paragraph shall not subject the Route 66 National Historic Trail or any land on which the Route 66 National Historic Trail is located to any other Federal laws (including regulations) requiring a Federal permit or authorization that would otherwise be made applicable as a result of the designation of the Route 66 National Historic Trail as a component of the National Trails System. .",
      "versionDate": "2025-09-18",
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
        "updateDate": "2025-12-01T16:31:12Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5470ih.xml"
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
      "title": "Route 66 National Historic Trail Designation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Route 66 National Historic Trail Designation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Trails System Act to designate the Route 66 National Historic Trail, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:31Z"
    }
  ]
}
```
