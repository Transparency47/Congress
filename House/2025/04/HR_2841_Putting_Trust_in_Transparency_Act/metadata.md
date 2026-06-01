# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2841?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2841
- Title: Putting Trust in Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 2841
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2025-05-24T08:05:49Z
- Update date including text: 2025-05-24T08:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2841",
    "number": "2841",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000565",
        "district": "9",
        "firstName": "Paul",
        "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
        "lastName": "Gosar",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Putting Trust in Transparency Act",
    "type": "HR",
    "updateDate": "2025-05-24T08:05:49Z",
    "updateDateIncludingText": "2025-05-24T08:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "OK"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TN"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TX"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "SC"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "CO"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2841ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2841\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Gosar (for himself, Mr. Biggs of Arizona , Mr. Brecheen , Mr. Burchett , Mr. Crane , Mr. Nehls , Mr. Norman , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to require the public disclosure of the names and partial addresses of contributors to 501(c) organizations that receive Federal funding.\n#### 1. Short title\nThis Act may be cited as the Putting Trust in Transparency Act .\n#### 2. Findings and Sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nIn the United States, nongovernmental organizations, or NGOs, often assist the Federal government with distribution of resources to the American People and abroad.\n**(2)**\nThe executive Memo entitled Memorandum for the Heads of Executive Departments and Agencies , published February 6, 2025, requires executive departments and agencies to review all Federal funding to nongovernmental organizations; however, this review does not apply to these organizations\u2019 non-Federal sources of funding.\n**(3)**\nThe non-Federal sources of NGOs\u2019 extravagant revenue are already reported to the Internal Revenue Service through the Form 990 Schedule B, but these Forms are not shared government wide.\n**(4)**\nArticle I, Section 8 of the U.S. Constitution empowers Congress to make rules for the government and regulate the use of taxpayer dollars.\n**(5)**\nNGOs that operate independently of the Federal government and any Federal grants or contributions of any amount are not subject to rigorous Congressional oversight and face limited restrictions on expression and association.\n**(6)**\nTo empower lawmakers to make responsible decisions with Americans\u2019 tax dollars and provide transparency to the American People, all Americans should have access to the megadonors of NGOs that leverage Federal dollars for their own agenda.\n##### (b) Sense of Congress\nIt is the sense of Congress that any nongovernmental organization that receives Federal funding of any kind is acting on behalf of the United States government and subject to the same fiscal oversight requirements as executive agencies.\n#### 3. Annual disclosure of contributors to exempt organizations\n##### (a) Amendments to Internal Revenue Code of 1986\n**(1) Public disclosure of names and partial addresses of donors**\nSection 6104 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby inserting (except as provided in subsection (e)) after name or address each place it appears, and\n**(B)**\nby adding at the end the following new subsection:\n(e) Public disclosure of Form 990 In the case of an organization described in subsection (c) of section 501 and exempt from taxation under section 501(a) which receives Federal funding during the taxable year, the Secretary shall make public any schedule B of Form 990 (or successor Form) filed by such organization\u2014 (1) within 60 days of processing such Form, and (2) with the name, zip code, and total contribution of any contributor unredacted. .\n**(2) Loss of exempt status for failure to file schedule B of Form 990**\nSection 6033(j) of such Code is amended by adding at the end the following new paragraph:\n(4) Revocation of exempt status for failure to file schedule B of Form 990 (A) Notice If an organization described in subsection (e) fails to file the Form required under such subsection by the due date for the return of tax for such organization for the taxable year, the Secretary shall notify the organization\u2014 (i) that the Internal Revenue Service has no record of such a return or notice from such organization, and (ii) about the revocation that will occur under subparagraph (B) if the organization fails to file such a return or notice within 60 days of such notification. (B) Revocation If an organization described in subsection (e) fails to file schedule B of Form 990 of the Internal Revenue Service (or any successor schedule or Form) with the return or notice of such organization for the taxable year, such organization's status as an organization exempt from tax under section 501(a) shall be considered revoked on and after the date set by the Secretary under subparagraph (A)(ii). The Secretary shall publish and maintain a list of any organization the status of which is so revoked. .\n##### (b) Application necessary for reinstatement; Retroactive reinstatement allowed if cause shown\nSection 6033(j) of such Code is amended by striking paragraph (1) each place it appears and inserting paragraph (1) or (4) .\n##### (c) Effective date\nThe amendments made by this section shall apply to returns filed for taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-04-10",
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
        "name": "Taxation",
        "updateDate": "2025-05-12T20:43:06Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2841ih.xml"
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
      "title": "Putting Trust in Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-26T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Putting Trust in Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-26T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to require the public disclosure of the names and partial addresses of contributors to 501(c) organizations that receive Federal funding.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-26T03:48:25Z"
    }
  ]
}
```
