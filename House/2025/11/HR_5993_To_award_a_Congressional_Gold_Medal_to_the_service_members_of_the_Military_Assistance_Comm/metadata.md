# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5993?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5993
- Title: MACV–SOG Congressional Gold Medal Act
- Congress: 119
- Bill type: HR
- Bill number: 5993
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-04-16T08:06:39Z
- Update date including text: 2026-04-16T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-10 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-10 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5993",
    "number": "5993",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "A000379",
        "district": "4",
        "firstName": "Mark",
        "fullName": "Rep. Alford, Mark [R-MO-4]",
        "lastName": "Alford",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "MACV\u2013SOG Congressional Gold Medal Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:39Z",
    "updateDateIncludingText": "2026-04-16T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-10T17:02:50Z",
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "False",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5993ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5993\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mr. Alford (for himself, Mr. Carbajal , and Mr. Jackson of Texas ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo award a Congressional Gold Medal to the service members of the Military Assistance Command Vietnam-Studies and Observations Group, in recognition of their bravery and outstanding service in South Vietnam, North Vietnam, Laos, and Cambodia during the Vietnam War.\n#### 1. Short title\nThis Act may be cited as the MACV\u2013SOG Congressional Gold Medal Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Military Assistance Command Vietnam-Studies and Observations Group (referred to in this Act as MACV\u2013SOG ) was established in January 1964 as a dedicated joint military task force to conduct high risk and special activities in the denied areas of North Vietnam, Laos, and Cambodia.\n**(2)**\nMACV\u2013SOG conducted deep-penetration reconnaissance, sabotage, direct-action mission, rescue missions for downed pilots, prisoner-of-war snatches, bomb-damage assessments, wiretaps, psychological operations, and maritime operations against the North Vietnamese.\n**(3)**\nMACV\u2013SOG remains one of the most distinguished and elite special operations units in United States military history, setting standards for modern special operations forces. Twelve MACV\u2013SOG operators have been awarded the Congressional Medal of Honor.\n**(4)**\nBetween 1964 and 1972, approximately 1,579 people of the United States are listed as missing or killed while serving with MACV\u2013SOG. This accounts for more than \u00bd of all Green Beret fatalities during the Vietnam War and more than 50 MACV\u2013SOG team members are still missing in action.\n**(5)**\nThe innovative tactics of MACV\u2013SOG, integration with indigenous forces, and mastery of direct action and special warfare created a blueprint for modern special operations. Many of the strategies, technologies, and doctrines they pioneered are now standard across elite military units, reinforcing their legacy as a cornerstone of United States special operations history.\n**(6)**\nMACV\u2013SOG created battlefield effects that were vastly disproportionate to the small size of the command. The impact of MACV\u2013SOG on the North Vietnamese logistics, troop deployment, and morale was profound. The North Vietnamese diverted entire divisions, as many as 50,000 troops, and numerous other resources away from offensive operations to defend against incursions by MACV\u2013SOG and to internal security operations in North Vietnam.\n**(7)**\nThese covert operations remained unacknowledged by military leadership and unknown to the United States public, until their existence began to be declassified decades later. This secret war denied MACV\u2013SOG members their just recognition and deprived the families of deceased and wounded operators from knowing the full extent of the sacrifice of their loved ones to the United States.\n**(8)**\nMACV\u2013SOG was a joint operations program that included members of the Army Special Forces, Navy SEALs, Force Reconnaissance Marines, the United States Air Force, and the Central Intelligence Agency.\n**(9)**\nMACV\u2013SOG teams also relied heavily on the indigenous population, including Montagnards, Chinese Nung, Cambodian, and Vietnamese personnel, along with the 219th Vietnamese Air Force King Bee helicopter pilots, who were actively engaging in the fight against communist forces.\n**(10)**\nTwelve Medal of Honor recipients have been recognized for their gallantry during actions while operating with MACV\u2013SOG units.\n**(11)**\nA Presidential Unit Citation was issued to MACV\u2013SOG by President George W. Bush in 2001.\n**(12)**\nThe bravery, sacrifice, and quiet professionalism of MACV\u2013SOG units from 1964 to 1972 reflect favorably upon the highest traditions of the United States military and the United States.\n#### 3. Congressional gold medal\n##### (a) Presentation authorized\nThe Speaker of the House of Representatives and the President pro tempore of the Senate shall make appropriate arrangements for the presentation, on behalf of Congress, of a single gold medal of appropriate design to the service members of MACV\u2013SOG, in recognition of their bravery and outstanding service in South Vietnam, North Vietnam, Laos, and Cambodia during the Vietnam War.\n##### (b) Design and striking\nFor the purposes of the presentation referred to in subsection (a), the Secretary of the Treasury (referred to in this Act as the Secretary ) shall strike a gold medal with suitable emblems, devices, and inscriptions, to be determined by the Secretary.\n##### (c) Smithsonian Institution\n**(1) In general**\nFollowing the presentation of the gold medal referred to in subsection (a), the gold medal shall be given to the Smithsonian Institution, where it will be available for display as appropriate and available for research.\n**(2) Sense of Congress**\nIt is the sense of Congress that the Smithsonian Institution should make the gold medal awarded pursuant to this Act available for display elsewhere, particularly at appropriate locations and events associated with MACV\u2013SOG.\n#### 4. Duplicate medals\nThe Secretary may strike and sell duplicates in bronze of the gold medal struck under section 3, at a price sufficient to cover the costs thereof, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 5. Status of medals\n##### (a) National medal\nMedals struck pursuant to this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic items\nFor purposes of sections 5134 and 5136 of title 31, United States Code, all medals struck under this Act shall be considered to be numismatic items.\n#### 6. Authority to use fund amounts; proceeds of sale\n##### (a) Authority To use fund amounts\nThere is authorized to be charged against the United States Mint Public Enterprise Fund such amounts as may be necessary to pay for the costs of the medals struck under this Act.\n##### (b) Proceeds of sale\nAmounts received from the sale of duplicate bronze medals authorized under section 4 shall be deposited into the United States Mint Public Enterprise Fund.",
      "versionDate": "2025-11-10",
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
        "actionDate": "2025-06-05",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1970",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MACV\u2013SOG Congressional Gold Medal Act",
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
        "updateDate": "2025-11-19T16:58:00Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5993ih.xml"
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
      "title": "MACV\u2013SOG Congressional Gold Medal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MACV\u2013SOG Congressional Gold Medal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To award a Congressional Gold Medal to the service members of the Military Assistance Command Vietnam-Studies and Observations Group, in recognition of their bravery and outstanding service in South Vietnam, North Vietnam, Laos, and Cambodia during the Vietnam War.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:20Z"
    }
  ]
}
```
