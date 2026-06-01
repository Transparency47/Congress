# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4251?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4251
- Title: Protecting Americans from Reckless Gun Dealers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4251
- Origin chamber: House
- Introduced date: 2025-06-30
- Update date: 2025-07-28T12:40:52Z
- Update date including text: 2025-07-28T12:40:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-30: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-30: Introduced in House

## Actions

- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-30",
    "latestAction": {
      "actionDate": "2025-06-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4251",
    "number": "4251",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Protecting Americans from Reckless Gun Dealers Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-28T12:40:52Z",
    "updateDateIncludingText": "2025-07-28T12:40:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-30",
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
      "actionDate": "2025-06-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-30",
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
          "date": "2025-06-30T18:00:15Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "DC"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "NY"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4251ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4251\nIN THE HOUSE OF REPRESENTATIVES\nJune 30, 2025 Ms. Brownley (for herself, Ms. Norton , and Mr. Goldman of New York ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require the Attorney General to report certain revocation and remedial action data with respect to Federal firearm licenses and to require the Comptroller General of the United States to study the effectiveness of the Bureau of Alcohol, Tobacco, Firearms and Explosives in investigating and revoking the licenses.\n#### 1. Short title\nThis Act may be cited as the Protecting Americans from Reckless Gun Dealers Act of 2025 .\n#### 2. Annual report of the Attorney General\n##### (a) In general\nChapter 44 of title 18, United States Code is amended by inserting after section 925D the following:\n925E. Annual report to Congress on license inspections. (a) In general Within 180 days after the date of the enactment of this section, and annually thereafter, the Attorney General shall submit to the appropriate congressional committees a written report on the actions undertaken by the Bureau of Alcohol, Tobacco, Firearms, and Explosives in the year covered by the report to issue and revoke licenses and inspect licensees under section 923, that includes the following: (1) The number of inspections completed each month. (2) The number of inspections that identified at least 1 serious violation. (3) The number of licenses that were revoked, the number of licenses that were not renewed in lieu of revocation, and the number of licenses surrendered after an inspection. (4) For each licensee whose license was revoked on the basis of an inspection, the name and location of the licensee, the date of revocation, and any serious violation identified by the inspection. (5) For each licensee whose license was not renewed in lieu of revocation after an inspection, the name and location of the licensee, the date the license expired, and any serious violation identified by the inspection. (6) For each licensee who surrendered such a license after an inspection, including a licensee who discontinued business operations, the name and location of the licensee, the date of surrender, and any serious violation identified by the inspection. (7) The number of inspections that identified at least 1 serious violation but with respect to which the Attorney General did not revoke the applicable license, broken down by\u2014 (A) the Attorney General\u2019s decision not to pursue revocation, further broken down by the Attorney General\u2019s reason for the decision; (B) the reversal of an initial decision of the Attorney General to revoke the license after a hearing held pursuant to section 923(f)(2); and (C) the order of a court to reverse a revocation after a petition was filed for review of a final agency determination. (8) The reasons of the Attorney General not to pursue revocation, broken down geographically based on the location of the field office of the Bureau with responsibility for the area where the licensee involved is located. (9) The number of reports of violations and warning letters issued and warning conferences held by the Bureau, broken down geographically based on the location of the field office of the Bureau involved. (b) Publication on website On each date a report required by subsection (a) is submitted, the Attorney General shall cause to be published on the website of the Bureau the information contained in the report. (c) Appropriate congressional committees In this section, the term appropriate congressional committees means\u2014 (1) the Committee on the Judiciary of the House of Representatives; and (2) the Committee on the Judiciary of the Senate. (d) Serious violation In this section, the term serious violation means one of the following: (1) Refusing to allow an inspection pursuant to section 923(g). (2) Transferring a firearm in violation of section 922(d). (3) Failing to wait 3 business days before transferring a firearm pursuant to section 922(t)(1). (4) Failing to comply with any other requirement of section 922(t)(1) before transferring a firearm. (5) Falsifying a record required to be maintained pursuant to section 923(g). (6) Failing to respond to a trace request pursuant to section 923(g)(7). (7) Transferring a firearm to another person with the knowledge that the person is making a straw purchase of the firearm in violation of section 932. (8) Failing to submit a report of multiple sales or other dispositions to an unlicensed person pursuant to section 923(g)(3). (9) Failing to report a theft or loss of a firearm pursuant to section 923(g)(6). (10) Failing to maintain an accurate record of the receipt, sale, or other disposition of a firearm pursuant to section 923(g)(2). .\n##### (b) Clerical amendment\nThe table of contents for such chapter is amended by inserting after the item relating to section 925D the following:\n925E. Annual report to Congress on license inspections. .\n#### 3. GAO study and report on the effectiveness of the Bureau of Alcohol, Tobacco, Firearms, and Explosives to investigate Federal firearm licenses\n##### (a) Study\nThe Comptroller General of the United States shall conduct a study on the operations and procedures used to issue and revoke licenses under section 923 of title 18, United States Code, and to investigate and inspect holders of such licenses, that focuses on\u2014\n**(1)**\nwhether systemic failures in the issuance and revocation of the licenses have resulted in ineffective enforcement of chapter 44 of such title;\n**(2)**\nthe extent to which the Attorney General has exercised discretion not to pursue revocation of a license based on the putative existence of extraordinary circumstances, notwithstanding a finding by the Attorney General that a licensee willfully committed a violation that renders the license eligible for revocation;\n**(3)**\ngeographic variability in the enforcement of such chapter;\n**(4)**\nthe outcomes related to the revocation of licenses, including\u2014\n**(A)**\nthe number of licensees who received a notice of license revocation but whose licenses were not revoked; and\n**(B)**\nthe average and median periods of time from inspection to revocation of a license, broken down by\u2014\n**(i)**\nrevocations without hearing or appeal by the licensee;\n**(ii)**\nrevocations after an administrative determination without judicial review pursued by the licensee; and\n**(iii)**\nrevocations after such a judicial review; and\n**(5)**\nthe policies and practices for providing oversight of the activities of the licensees during the pendency of revocation proceedings, including while a licensee seeks judicial review.\n##### (b) Report to Congress\nWithin 1 year after the date of the enactment of this Act, the Comptroller General of the United States shall submit a written report to Congress on the results of the study required by subsection (a).",
      "versionDate": "2025-06-30",
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
        "updateDate": "2025-07-28T12:40:52Z"
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
      "date": "2025-06-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4251ih.xml"
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
      "title": "Protecting Americans from Reckless Gun Dealers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Americans from Reckless Gun Dealers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Attorney General to report certain revocation and remedial action data with respect to Federal firearm licenses and to require the Comptroller General of the United States to study the effectiveness of the Bureau of Alcohol, Tobacco, Firearms and Explosives in investigating and revoking the licenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T05:33:37Z"
    }
  ]
}
```
