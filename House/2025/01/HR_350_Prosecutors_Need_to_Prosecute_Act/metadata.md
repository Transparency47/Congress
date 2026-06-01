# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/350?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/350
- Title: Prosecutors Need to Prosecute Act
- Congress: 119
- Bill type: HR
- Bill number: 350
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-11-01T08:05:40Z
- Update date including text: 2025-11-01T08:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/350",
    "number": "350",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Prosecutors Need to Prosecute Act",
    "type": "HR",
    "updateDate": "2025-11-01T08:05:40Z",
    "updateDateIncludingText": "2025-11-01T08:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:05:35Z",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "PA"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "GA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr350ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 350\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Ms. Malliotakis (for herself, Mr. Weber of Texas , Ms. Van Duyne , Mr. Ellzey , Mr. Joyce of Pennsylvania , Mr. Issa , and Mr. Loudermilk ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act to direct district attorney and prosecutors offices to report to the Attorney General, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prosecutors Need to Prosecute Act .\n#### 2. District attorney reporting requirements for Byrne grants\nSection 501 of subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 ) is amended\u2014\n**(1)**\nby redesignating subsections (g) and (h) as subsections (h) and (i), respectively; and\n**(2)**\nby inserting after subsection (f) the following:\n(g) District Attorney Reporting Requirements (1) In general On an annual basis, each chief executive of a district attorney or prosecutor\u2019s office that serves a jurisdiction of 380,000 or more persons, which jurisdiction receives funds under this part, shall submit to the Attorney General a report that contains, for the previous fiscal year, the following: (A) The total number of cases referred to the office for prosecution of a covered offense. (B) The number of cases such office declined to prosecute involving a covered offense. (C) For cases involving a covered offense that resulted in a plea agreement reached with the defendant\u2014 (i) the total number of such cases; (ii) the number of such cases by each initial charge; and (iii) the number of such cases by each charge of conviction. (D) The number of cases involving covered offenses initiated against a defendant\u2014 (i) previously arrested for a covered offense arising out of separate conduct; (ii) previously convicted for a covered offense arising out of separate conduct; (iii) with an open case involving a covered offense arising out of separate conduct; (iv) serving a term of probation for a conviction for a covered offense arising out of separate conduct; and (v) released on parole for a conviction for a covered offense arising out of separate conduct. (E) The number of defendants charged with a covered offense\u2014 (i) who were released on their own recognizance; (ii) who were eligible for bail; and (iii) for whom the prosecutor requested bail. (2) Uniform standards The Attorney General shall define uniform standards for the reporting of the information required under this subsection, including the form such reports shall take and the process by which such reports shall be shared with the Attorney General. (3) Submission to Judiciary Committees The Attorney General shall submit the information received under this subsection to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives and shall publish such information on a publicly viewable website. (4) Covered offense defined In this subsection, the term covered offense means any of the following: (A) Murder or non-negligent manslaughter. (B) Forcible rape. (C) Robbery. (D) Aggravated assault. (E) Burglary. (F) Larceny. (G) Motor vehicle theft. (H) Arson. (I) Any offense involving the illegal use of a firearm. (J) Any offense involving the illegal possession of a firearm. .",
      "versionDate": "2025-01-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2025-02-13T16:24:50Z"
          },
          {
            "name": "Crimes against property",
            "updateDate": "2025-02-13T16:24:50Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-02-13T16:24:50Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-02-13T16:24:50Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-13T16:24:50Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-02-13T16:24:50Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-02-13T16:24:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-13T15:48:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr350",
          "measure-number": "350",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-04-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr350v00",
            "update-date": "2025-04-22"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Prosecutors Need to Prosecute Act</b></p> <p>This bill requires certain state and local prosecutors to report data on criminal referrals and outcomes of cases involving murder or non-negligent manslaughter, forcible rape, robbery, aggravated assault, burglary, larceny, motor vehicle theft, arson, or any offense involving the illegal use or possession of a firearm. </p> <p>The reporting requirement applies to state and local prosecutors in a jurisdiction with 380,000 or more persons that receives funding under the Edward Byrne Memorial Justice Assistance Grant program. The report must contain data on</p> <ul> <li>cases referred for prosecution, </li> <li>cases declined for prosecution,</li> <li>cases resulting in a plea agreement with the defendant,</li> <li>cases initiated against defendants with previous arrests or convictions, and</li> <li>defendants charged who were released or eligible for bail. </li> </ul>"
        },
        "title": "Prosecutors Need to Prosecute Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr350.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Prosecutors Need to Prosecute Act</b></p> <p>This bill requires certain state and local prosecutors to report data on criminal referrals and outcomes of cases involving murder or non-negligent manslaughter, forcible rape, robbery, aggravated assault, burglary, larceny, motor vehicle theft, arson, or any offense involving the illegal use or possession of a firearm. </p> <p>The reporting requirement applies to state and local prosecutors in a jurisdiction with 380,000 or more persons that receives funding under the Edward Byrne Memorial Justice Assistance Grant program. The report must contain data on</p> <ul> <li>cases referred for prosecution, </li> <li>cases declined for prosecution,</li> <li>cases resulting in a plea agreement with the defendant,</li> <li>cases initiated against defendants with previous arrests or convictions, and</li> <li>defendants charged who were released or eligible for bail. </li> </ul>",
      "updateDate": "2025-04-22",
      "versionCode": "id119hr350"
    },
    "title": "Prosecutors Need to Prosecute Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Prosecutors Need to Prosecute Act</b></p> <p>This bill requires certain state and local prosecutors to report data on criminal referrals and outcomes of cases involving murder or non-negligent manslaughter, forcible rape, robbery, aggravated assault, burglary, larceny, motor vehicle theft, arson, or any offense involving the illegal use or possession of a firearm. </p> <p>The reporting requirement applies to state and local prosecutors in a jurisdiction with 380,000 or more persons that receives funding under the Edward Byrne Memorial Justice Assistance Grant program. The report must contain data on</p> <ul> <li>cases referred for prosecution, </li> <li>cases declined for prosecution,</li> <li>cases resulting in a plea agreement with the defendant,</li> <li>cases initiated against defendants with previous arrests or convictions, and</li> <li>defendants charged who were released or eligible for bail. </li> </ul>",
      "updateDate": "2025-04-22",
      "versionCode": "id119hr350"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr350ih.xml"
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
      "title": "Prosecutors Need to Prosecute Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prosecutors Need to Prosecute Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act to direct district attorney and prosecutors offices to report to the Attorney General, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:17Z"
    }
  ]
}
```
