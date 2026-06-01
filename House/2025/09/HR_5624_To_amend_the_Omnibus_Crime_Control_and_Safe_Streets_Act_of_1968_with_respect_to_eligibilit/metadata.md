# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5624?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5624
- Title: No Funding for Lawless Jurisdictions Act
- Congress: 119
- Bill type: HR
- Bill number: 5624
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-12-16T16:27:07Z
- Update date including text: 2025-12-16T16:27:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5624",
    "number": "5624",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001102",
        "district": "8",
        "firstName": "Mark",
        "fullName": "Rep. Harris, Mark [R-NC-8]",
        "lastName": "Harris",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "No Funding for Lawless Jurisdictions Act",
    "type": "HR",
    "updateDate": "2025-12-16T16:27:07Z",
    "updateDateIncludingText": "2025-12-16T16:27:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "AZ"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "OH"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NC"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "OK"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IL"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "SC"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NC"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "SC"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "SC"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "AZ"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "NC"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5624ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5624\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Harris of North Carolina (for himself, Mr. Biggs of Arizona , Mr. Roy , Mr. Taylor , Mr. Murphy , Mr. Brecheen , Mrs. Miller of Illinois , Mr. Norman , Mr. Edwards , Mrs. Biggs of South Carolina , and Mr. Self ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 with respect to eligibility for certain crime control grants.\n#### 1. Short title\nThis Act may be cited as the No Funding for Lawless Jurisdictions Act .\n#### 2. Eligible entities for certain grants\nThe Omnibus Crime Control and Safe Streets Act of 1968 is amended\u2014\n**(1)**\nin section 502 ( 34 U.S.C. 10153 ) by adding at the end the following:\n(c) Eligibility (1) Certain entities prohibited Beginning the first fiscal year after the date of enactment of this subsection, and each fiscal year thereafter, the Attorney General may not award, renew, or extend a grant under this subpart to a State or unit of local government that has in effect a policy or law that\u2014 (A) substantially limits cash bail as a potential condition for every individual charged with a covered offense in the State or the area under the jurisdiction of the unit of local government; or (B) permits a judge or magistrate to grant pretrial release of an individual previously convicted of a felony on personal recognizance. (2) Covered offense defined In this subsection, the term covered offense means a criminal offense that poses a clear threat to public safety and order, including\u2014 (A) an offense involving a violent or sexual act, such as murder, rape, sexual assault, carjacking, robbery, burglary, and assault; and (B) an offense that promotes public disorder, such as looting, vandalism, destruction of property, rioting or inciting to riot, or fleeing from a law enforcement officer. ; and\n**(2)**\nin section 1702 ( 34 U.S.C. 10382 ) by adding at the end the following:\n(e) Eligibility (1) Certain entities prohibited Beginning the first fiscal year after the date of enactment of this subsection, and each fiscal year thereafter, the Attorney General may not award, renew, or extend a grant under this subpart to a covered jurisdiction that has reduced a law enforcement agency\u2019s budget in the previous fiscal year, unless such reduction is the result of an overall budget shortfall applied proportionately across all government departments. (2) Covered jurisdiction defined In this subsection, the term covered jurisdiction means a unit of local government that is also an urbanized area, as defined by the United States Census Bureau. .",
      "versionDate": "2025-09-30",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-16T16:27:07Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5624ih.xml"
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
      "title": "No Funding for Lawless Jurisdictions Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T07:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Funding for Lawless Jurisdictions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T07:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 with respect to eligibility for certain crime control grants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T07:33:29Z"
    }
  ]
}
```
