# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/234?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/234
- Title: Prosecutors Need to Prosecute Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 234
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/234",
    "number": "234",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Prosecutors Need to Prosecute Act of 2025",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T22:29:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s234is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 234\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Kennedy (for himself and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to direct certain prosecutor's offices to annually report to the Attorney General, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prosecutors Need to Prosecute Act of 2025 .\n#### 2. District attorney and prosecutor reports\nSection 501 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 ) is amended\u2014\n**(1)**\nby redesignating subsections (g) and (h) as subsections (h) and (i), respectively; and\n**(2)**\nby inserting after subsection (f) the following:\n(f) District attorney reporting requirements (1) Definitions In this subsection: (A) Covered offense The term covered offense means any of the following: (i) Murder or non-negligent manslaughter. (ii) Forcible rape. (iii) Robbery. (iv) Aggravated assault. (v) Burglary. (vi) Larceny. (vii) Motor vehicle theft. (viii) Arson. (ix) Any offense involving the illegal use of a firearm. (x) Any offense involving the illegal possession of a firearm. (B) Covered prosecutor The term covered prosecutor means the chief executive of a district attorney or prosecutor\u2019s office that serves a local government\u2014 (i) the population of the jurisdiction of which is not less than 360,000 individuals; and (ii) that receives funds under this part. (2) Reporting requirement Not later than 1 year after the date of enactment of the Prosecutors Need to Prosecute Act of 2025 , and annually thereafter, a covered prosecutor shall submit to the Attorney General a report that contains, for the previous fiscal year, the following: (A) The total number of cases referred to the covered prosecutor for prosecution of a covered offense. (B) The number of cases involving a covered offense\u2014 (i) that the covered prosecutor declined to prosecute or refer for diversion; or (ii) for which the covered prosecutor declined to reach a plea agreement. (C) For cases involving a covered offense that result in a plea agreement or referral for diversion reached with the defendant, the number of cases for which the defendant\u2014 (i) was previously arrested for a covered offense arising out of a separate conviction; (ii) was previously convicted for a covered offense arising out of a separate conviction; (iii) is involved in an open case involving a covered offense arising out of separate conduct; (iv) is serving a term of probation for a conviction for a covered offense arising out of separate conduct; and (v) was released on parole for a conviction for a covered offense arising out of separate conduct. (D) The number of covered offenses that the covered prosecutor does not prosecute as a result of an internal policy against prosecuting specific criminal offenses, including\u2014 (i) each covered offense captured in the internal policy; and (ii) each criminal offense that is not captured in the internal policy. (3) Compliance With respect to a covered prosecutor that complies with the requirement under paragraph (2)\u2014 (A) the Attorney General shall give priority in disbursing funds under this part to the local government served by the covered prosecutor; and (B) the local government described in subparagraph (A) shall ensure that the covered prosecutor receives a portion of the funds received under this part. (4) Uniform standards The Attorney General shall establish uniform standards for the reporting of the information required under this subsection, including the form such reports shall take and the process by which such reports shall be shared with the Attorney General. (5) Submission to judiciary committees The Attorney General shall\u2014 (A) submit the information received under this subsection to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives; and (B) publish such information on a publicly viewable website. .\n#### 3. Byrne-JAG funds and elimination of cash bail\nThe Attorney General shall not distribute amounts under subpart I of part E of title 1 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ) to a State or local government that has in effect a policy that prohibits the use of cash bail for a defendant in a case involving the illegal use or illegal possession of a firearm.",
      "versionDate": "2025-01-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2025-03-21T19:56:50Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-21T19:57:28Z"
          },
          {
            "name": "Crimes against property",
            "updateDate": "2025-03-21T19:56:57Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-03-21T19:56:30Z"
          },
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-03-21T19:56:37Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-03-21T19:57:34Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-03-21T19:57:06Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-21T19:57:13Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-03-21T19:57:19Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-03-21T19:57:24Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-03-21T19:57:01Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-21T19:56:24Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-03-21T19:56:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-24T20:20:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
    "originChamber": "Senate",
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
          "measure-id": "id119s234",
          "measure-number": "234",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s234v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Prosecutors Need to Prosecute Act of 2025\u00a0</strong></p><p>This bill requires certain state and local prosecutors to report data on criminal referrals and outcomes of cases involving murder or non-negligent manslaughter, forcible rape, robbery, aggravated assault, burglary, larceny, motor vehicle theft, arson, or any offense involving the illegal use or possession of a firearm.</p><p>The reporting requirement applies to state and local prosecutors in a jurisdiction that has 360,000 or more persons and receives funding under the Edward Byrne Memorial Justice Assistance Grant (JAG) program. The report must contain data on</p><ul><li>cases referred for prosecution,</li><li>cases the prosecutor declined to prosecute or refer for diversion,</li><li>cases for which the prosecutor declined to reach a plea agreement,</li><li>cases that resulted in a plea agreement or referral for diversion, and</li><li>offenses the prosecutor did not prosecute due to an internal policy.</li></ul><p>If a state or local prosecutor complies with these requirements, the bill requires (1) the Department of Justice to give priority in disbursing Byrne JAG program funds to the local government served by the prosecutor, and (2) the local government to ensure that the prosecutor receives a portion of the funds.</p><p>Additionally, the bill prohibits states and local governments from receiving funds under the Byrne JAG program if they have in effect a policy that prohibits the use of cash bail for a defendant in a case involving the illegal use or illegal possession of a firearm.</p>"
        },
        "title": "Prosecutors Need to Prosecute Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s234.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prosecutors Need to Prosecute Act of 2025\u00a0</strong></p><p>This bill requires certain state and local prosecutors to report data on criminal referrals and outcomes of cases involving murder or non-negligent manslaughter, forcible rape, robbery, aggravated assault, burglary, larceny, motor vehicle theft, arson, or any offense involving the illegal use or possession of a firearm.</p><p>The reporting requirement applies to state and local prosecutors in a jurisdiction that has 360,000 or more persons and receives funding under the Edward Byrne Memorial Justice Assistance Grant (JAG) program. The report must contain data on</p><ul><li>cases referred for prosecution,</li><li>cases the prosecutor declined to prosecute or refer for diversion,</li><li>cases for which the prosecutor declined to reach a plea agreement,</li><li>cases that resulted in a plea agreement or referral for diversion, and</li><li>offenses the prosecutor did not prosecute due to an internal policy.</li></ul><p>If a state or local prosecutor complies with these requirements, the bill requires (1) the Department of Justice to give priority in disbursing Byrne JAG program funds to the local government served by the prosecutor, and (2) the local government to ensure that the prosecutor receives a portion of the funds.</p><p>Additionally, the bill prohibits states and local governments from receiving funds under the Byrne JAG program if they have in effect a policy that prohibits the use of cash bail for a defendant in a case involving the illegal use or illegal possession of a firearm.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119s234"
    },
    "title": "Prosecutors Need to Prosecute Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prosecutors Need to Prosecute Act of 2025\u00a0</strong></p><p>This bill requires certain state and local prosecutors to report data on criminal referrals and outcomes of cases involving murder or non-negligent manslaughter, forcible rape, robbery, aggravated assault, burglary, larceny, motor vehicle theft, arson, or any offense involving the illegal use or possession of a firearm.</p><p>The reporting requirement applies to state and local prosecutors in a jurisdiction that has 360,000 or more persons and receives funding under the Edward Byrne Memorial Justice Assistance Grant (JAG) program. The report must contain data on</p><ul><li>cases referred for prosecution,</li><li>cases the prosecutor declined to prosecute or refer for diversion,</li><li>cases for which the prosecutor declined to reach a plea agreement,</li><li>cases that resulted in a plea agreement or referral for diversion, and</li><li>offenses the prosecutor did not prosecute due to an internal policy.</li></ul><p>If a state or local prosecutor complies with these requirements, the bill requires (1) the Department of Justice to give priority in disbursing Byrne JAG program funds to the local government served by the prosecutor, and (2) the local government to ensure that the prosecutor receives a portion of the funds.</p><p>Additionally, the bill prohibits states and local governments from receiving funds under the Byrne JAG program if they have in effect a policy that prohibits the use of cash bail for a defendant in a case involving the illegal use or illegal possession of a firearm.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119s234"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s234is.xml"
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
      "title": "Prosecutors Need to Prosecute Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:55Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prosecutors Need to Prosecute Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to direct certain prosecutor's offices to annually report to the Attorney General, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:19:02Z"
    }
  ]
}
```
