# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7462?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7462
- Title: Farmers’ AID Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 7462
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-02-19T18:44:26Z
- Update date including text: 2026-02-19T18:44:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7462",
    "number": "7462",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Farmers\u2019 AID Relief Act",
    "type": "HR",
    "updateDate": "2026-02-19T18:44:26Z",
    "updateDateIncludingText": "2026-02-19T18:44:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:01:35Z",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "GA"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7462ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7462\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Mr. Carter of Georgia (for himself, Mr. Bishop , and Mr. Allen ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Crop Insurance Act to direct the Secretary of Agriculture to use certain data sets when determining eligibility related to indemnity payments under the Hurricane Insurance Protection-Wind Index endorsement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farmers\u2019 Assistance and Immediate Disaster Relief Act or the Farmers\u2019 AID Relief Act .\n#### 2. Hurricane Insurance Protection-Wind Index endorsement\n##### (a) In general\nSection 508 of the Federal Crop Insurance Act ( 7 U.S.C. 1508 ) is amended by adding at the end the following:\n(q) Hurricane Insurance Protection-Wind Index endorsement (1) Determination of payment eligibility (A) In general Beginning with crop year 2027, in determining whether a county is eligible with respect to a hurricane weather event for an indemnity payment under HIP\u2013WI, the Secretary shall\u2014 (i) use the IBTrACS data set; or (ii) subject to subparagraph (B), use the alternative data set compiled pursuant to paragraph (2). (B) Condition for use of alternative data set For purposes of subparagraph (A)(ii), the Secretary may only use the alternative data set compiled pursuant to paragraph (2) if\u2014 (i) the data set specified in subparagraph (A)(i) is incomplete, as determined by the Secretary; and (ii) one of the following conditions is met: (I) A weather station operated by National Weather Service in the county subject to the determination of eligibility in subparagraph (A), or an adjacent county, was damaged. (II) Any other source of data for making such determination in such county or an adjacent county was damaged. (III) Any such station or other source provided incomplete data, as determined by the Secretary. (2) Compilation of alternative data set For purposes of determining eligibility under paragraph (1)(A)(ii), the Secretary shall compile, and make available to the public on the website of the Department related to HIP\u2013WI, an alternative data set for the hurricane weather event prompting such determination using data that\u2014 (A) is collected for a specified time period during such weather event, as determined by the Secretary; (B) contains the same types of data contained in the IBTrACS data set; and (C) is consistent with the form of such types of data, as determined by the Secretary. (3) Definitions In this subsection: (A) HIP\u2013WI The term HIP\u2013WI means the Hurricane Insurance Protection-Wind Index endorsement established in 2020 by the Risk Management Agency of the Department. (B) IBTrACS data set The term IBTrACS data set means the International Best Track Archive for Climate Stewardship data set from the National Oceanic and Atmospheric Administration, including the season, name, time, location in latitude and longitude, maximum sustained winds, hurricane category, and wind extents data associated with a hurricane weather event. (C) Alternative data set The term alternative data set means data collected by a weather station that is\u2014 (i) operated by a land-grant college or university (as defined in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 )); and (ii) certified, at the time data is collected for purposes of paragraph (2), as compliant with standards issued by the National Weather Service, including the standards described in the directive issued on November 9, 2023, entitled National Weather Service Instruction 10\u20131302 (or successor directives). .\n##### (b) Regulations\nNot later than 180 days after the date of enactment of this Act, the Secretary of Agriculture shall\u2014\n**(1)**\nissue such rules as may be necessary to implement the amendment made by this section; and\n**(2)**\nrevise any guidance relating to the Hurricane Insurance Protection-Wind Index endorsement established in 2020 by the Risk Management Agency of the Department of Agriculture.",
      "versionDate": "2026-02-10",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-02-19T18:44:25Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7462ih.xml"
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
      "title": "Farmers\u2019 AID Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T09:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Farmers\u2019 AID Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T09:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Farmers\u2019 Assistance and Immediate Disaster Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T09:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Crop Insurance Act to direct the Secretary of Agriculture to use certain data sets when determining eligibility related to indemnity payments under the Hurricane Insurance Protection-Wind Index endorsement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T09:48:25Z"
    }
  ]
}
```
