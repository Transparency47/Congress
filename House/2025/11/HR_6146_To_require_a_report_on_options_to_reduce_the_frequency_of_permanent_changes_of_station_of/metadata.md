# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6146?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6146
- Title: STAY Act
- Congress: 119
- Bill type: HR
- Bill number: 6146
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2025-12-04T17:33:22Z
- Update date including text: 2025-12-04T17:33:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6146",
    "number": "6146",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "STAY Act",
    "type": "HR",
    "updateDate": "2025-12-04T17:33:22Z",
    "updateDateIncludingText": "2025-12-04T17:33:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "GA"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CT"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "NE"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6146ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6146\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mrs. Kiggans of Virginia (for herself and Mr. Bishop ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo require a report on options to reduce the frequency of permanent changes of station of members of the Armed Forces and the sea-shore rotations of such members, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Tours Across Years Act or the STAY Act .\n#### 2. Report on reducing frequency of permanent changes of station and naval vessel to onshore rotations\n##### (a) Report required\nNot later than March 1, 2026, the Under Secretary of Defense for Personnel and Readiness, in coordination with the Secretaries of the military departments, shall submit to the congressional defense committees a report on options to reduce the frequency of permanent changes of station of members of the Armed Forces and the rotations of such members between assignments to naval vessels and onshore assignments (commonly referred to as sea-shore rotations ).\n##### (b) Elements\nThe report under subsection (a) shall include the following:\n**(1)**\nAn analysis of the costs associated with the permanent changes of station and rotations specified in subsection (a), disaggregated by military department and occupational specialty, over the five fiscal years preceding the date of the report.\n**(2)**\nAn assessment of the potential cost savings of the Department of Defense to be realized through a reduction in the frequency of such permanent changes of station and rotations.\n**(3)**\nAn evaluation of the effects of a reduction in such frequency on retention of members of the Armed Forces, employment for the spouses of such members, and education of the children of such members.\n**(4)**\nAn identification of billets, duty stations, and communities with respect to which extended tour lengths or rotation adjustments would be operationally feasible while sustaining mission readiness and career progression requirements.\n**(5)**\nRecommendations for any legislative or policy changes necessary to conduct a pilot program for, or otherwise implement, extensions to tour lengths or rotation adjustments.\n##### (c) Congressional defense committees defined\nIn this section, the term congressional defense committees has the meaning given that term in section 101(a) of title 10, United States Code.",
      "versionDate": "2025-11-19",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-04T17:33:22Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6146ih.xml"
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
      "title": "STAY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T07:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STAY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Tours Across Years Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a report on options to reduce the frequency of permanent changes of station of members of the Armed Forces and the sea-shore rotations of such members, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T07:48:30Z"
    }
  ]
}
```
