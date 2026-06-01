# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/21?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/21
- Title: REMOTE Act
- Congress: 119
- Bill type: S
- Bill number: 21
- Origin chamber: Senate
- Introduced date: 2025-01-07
- Update date: 2026-04-09T15:34:58Z
- Update date including text: 2026-04-09T15:34:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in Senate
- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-07: Introduced in Senate

## Actions

- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/21",
    "number": "21",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "REMOTE Act",
    "type": "S",
    "updateDate": "2026-04-09T15:34:58Z",
    "updateDateIncludingText": "2026-04-09T15:34:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:26:19Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "OK"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s21is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 21\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2025 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require each Executive department to establish policies and collect information regarding teleworking employees of the Executive department, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Requiring Effective Management and Oversight of Teleworking Employees Act or the REMOTE Act .\n#### 2. Utilization data and reporting\n##### (a) Definitions\nIn this section:\n**(1) Agency office**\nThe term agency office means any office space\u2014\n**(A)**\nthat is owned or leased by an Executive department; and\n**(B)**\nin which not less than 1 employee of the Executive department described in subparagraph (A), or a contract employee with respect to that Executive department, regularly performs the duties of that employee or contract employee, as applicable.\n**(2) Budget justification materials**\nThe term budget justification materials has the meaning given the term in section 3(b)(2)(A) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note).\n**(3) Computer network**\nThe term computer network means software or a system\u2014\n**(A)**\nthat is operated by or for an Executive department; and\n**(B)**\nto which an employee of the Executive department described in subparagraph (A), or a contract employee with respect to that Executive department, is required to be digitally connected in order to work on behalf of that Executive department, such as to access the email account, user account, or file systems provided by the Executive department to that employee or contract employee, as applicable.\n**(4) Contract employee**\nThe term contract employee means an individual who\u2014\n**(A)**\nis not an employee of an Executive department;\n**(B)**\nis an employee of an entity that has entered into a contract with an Executive department; and\n**(C)**\nworks pursuant to the contract described in subparagraph (B).\n**(5) Executive department**\nThe term Executive department has the meaning given the term in section 101 of title 5, United States Code.\n**(6) Login**\nThe term login means the act by which an employee of an Executive department, or a contract employee with respect to an Executive department, makes a digital connection to a computer network with respect to that Executive department.\n**(7) Network traffic**\nThe term network traffic means the volume and flow of data across and within a computer network.\n**(8) Teleworking employee**\nThe term teleworking employee means an employee of an Executive department, or a contract employee with respect to an Executive department, who is\u2014\n**(A)**\nworking on behalf of the Executive department and not detailed to a different Federal entity; and\n**(B)**\ncovered by a telework agreement.\n**(9) Working remotely**\nThe term working remotely means, with respect to a teleworking employee, that the teleworking employee is performing work duties on a computer while located physically outside of an agency office with respect to the applicable Executive department (or, with respect to a contract employee, outside of office space owned or leased by the entity that employs the contract employee).\n##### (b) Data collection\nThe head of each Executive department shall\u2014\n**(1)**\nnot later than 180 days after the date of enactment of this Act, establish\u2014\n**(A)**\npolicies requiring the recording of the login activity of, and the network traffic that is generated by, each teleworking employee with respect to that Executive department; and\n**(B)**\ndirectives for managers of teleworking employees with respect to that Executive department to periodically review the network traffic generated by each such teleworking employee while that teleworking employee is working remotely; and\n**(2)**\nnot later than 1 year after the date of enactment of this Act\u2014\n**(A)**\nbegin retaining the data described in paragraph (1)(A), which shall include, with respect to each teleworking employee with respect to that Executive department who is working remotely\u2014\n**(i)**\nthe average number of logins made each day by the teleworking employee;\n**(ii)**\nthe average daily duration of the connection by the teleworking employee to the applicable computer network; and\n**(iii)**\nthe network traffic that such teleworking employee generates while working remotely; and\n**(B)**\nestablish a policy that the Executive department may dispose of data retained under subparagraph (A) not sooner than 3 years after the date on which the Executive department collects the data.\n##### (c) Swiped data collection\nBeginning on the date that is 180 days after the date of enactment of this Act, the head of each Executive department, with respect to each employee of the Executive department and each contract employee with respect to the Executive department who regularly performs the job duties of the employee or contract employee, as applicable, at the headquarters building of the Executive department\u2014\n**(1)**\nshall require that employee or contract employee to use a Personal Identity Verification Card or Common Access Card, as applicable, to make a login;\n**(2)**\nshall collect login data by that employee or contract employee using a Personal Identity Verification Card or Common Access Card, as applicable, which shall include, with respect to the employee or contract employee\u2014\n**(A)**\nthe average number of logins made each day by the employee or contract employee;\n**(B)**\nthe average daily duration of the connection by the employee or contract employee to the applicable computer network; and\n**(C)**\nthe network traffic that such employee or contract employee generates while working from the headquarters building;\n**(3)**\nshall retain data collected under paragraph (2); and\n**(4)**\nmay dispose of data retained under paragraph (3) not sooner than 3 years after the date on which the Executive department collects the data.\n##### (d) Report\nWith respect to the first fiscal year that begins after the date that is 180 days after the date of enactment of this Act, and with respect to each fiscal year thereafter, the head of each Executive department shall publish the data collected pursuant to subsections (b)(2)(A) and (c)(2) in the budget justification materials of the Executive department in a format that, for the applicable fiscal year\u2014\n**(1)**\nprotects personally identifiable information;\n**(2)**\ncompares the average login rates of teleworking employees working remotely on each weekday to the total number of teleworking employees approved to be working remotely on each weekday; and\n**(3)**\ncompares the average login rates of teleworking employees working remotely on each weekday to the average login rates of employees working from the headquarters building of the Executive department.\n#### 3. Chief Human Capital Officer reports\nSection 6506(d) of title 5, United States Code, is amended\u2014\n**(1)**\nby amending paragraph (1) to read as follows:\n(1) In general Each year, the Chief Human Capital Officer of each executive agency, in consultation with the Telework Managing Officer of that agency, shall submit a report to the Chair and Vice Chair of the Chief Human Capital Officers Council on agency management efforts to promote the efficient use of telework, which shall include a description of the adverse effects of telework policy on the performance of the executive agency, including any increased incidences of disciplinary actions against employees of the executive agency. ;\n**(2)**\nby redesignating paragraph (2) as paragraph (3); and\n**(3)**\nby inserting after paragraph (1) the following:\n(2) Collection and retention of relevant information Not later than 60 days after the date of enactment of the Requiring Effective Management and Oversight of Teleworking Employees Act , the Chief Human Capital Officer of each executive agency shall establish a policy that requires any manager of an employee of the executive agency who teleworks who revokes the privileges of that employee to telework due to a reason specific to that employee to provide written information to the human capital office of that executive agency (which shall retain that information for a reasonable amount of time after the employee is no longer employed by the executive agency) and to the employee regarding the circumstances giving rise to that revocation, which shall include\u2014 (A) the name, title, office, years of service, official worksite, and annual rate of basic pay of the employee; (B) the total number of days that the employee teleworked in the 6 work periods immediately preceding the work period in which the revocation occurred, which shall include an itemized identification of each day on which that employee teleworked during those 6 work periods; (C) a brief narrative summary of the circumstances giving rise to the revocation, with detail sufficient to confirm the propriety of the revocation under the policies of the executive agency; and (D) any steps the manager took to discipline the employee before carrying out the revocation. .",
      "versionDate": "2025-01-07",
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
            "name": "Commuting",
            "updateDate": "2025-02-03T17:19:48Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-02-03T17:19:48Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-09T15:34:58Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-02-03T17:19:48Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-03T17:20:06Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-02-03T17:19:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-01-27T23:00:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119s21",
          "measure-number": "21",
          "measure-type": "s",
          "orig-publish-date": "2025-01-07",
          "originChamber": "SENATE",
          "update-date": "2025-03-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s21v00",
            "update-date": "2025-03-12"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Requiring Effective Management and Oversight of Teleworking Employees Act or the REMOTE Act</strong></p><p>This bill directs executive agencies to track employees' computer network activity, compare the activity of teleworking and on-site employees,\u00a0and report on any\u00a0deficiencies in the performance of teleworking employees.</p><p>First, the bill requires each agency to establish policies to track for every employee (1) the average number of daily logins,\u00a0(2) the average daily duration of the network connection, and (3) the network traffic generated while the employee works. This information must be collected from employees working primarily on-site within 180 days after the bill's enactment and from teleworking employees within one year after the bill's enactment.\u00a0The bill also directs each agency to publish this data in the agency\u2019s fiscal year budget justification materials, including a comparison of the average login rates of\u00a0on-site and teleworking employees.</p><p>Next, the bill directs any manager who revokes\u00a0a teleworking employee's authorization to telework\u00a0(due to a reason specific to that employee)\u00a0to\u00a0document for the employee and the agency's Human Capital Office\u00a0(1) the total number of days that the employee teleworked in the six work periods immediately preceding the revocation, (2) a narrative summary of the circumstances giving rise to the revocation, and (3) any steps the manager took to discipline the employee before revoking the employee's telework authorization.\u00a0</p><p>Finally, agencies must report to the Chief Human Capital Officers Council\u00a0about any\u00a0adverse effects of telework\u00a0policies\u00a0on the performance of the executive agency. </p>"
        },
        "title": "REMOTE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s21.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Requiring Effective Management and Oversight of Teleworking Employees Act or the REMOTE Act</strong></p><p>This bill directs executive agencies to track employees' computer network activity, compare the activity of teleworking and on-site employees,\u00a0and report on any\u00a0deficiencies in the performance of teleworking employees.</p><p>First, the bill requires each agency to establish policies to track for every employee (1) the average number of daily logins,\u00a0(2) the average daily duration of the network connection, and (3) the network traffic generated while the employee works. This information must be collected from employees working primarily on-site within 180 days after the bill's enactment and from teleworking employees within one year after the bill's enactment.\u00a0The bill also directs each agency to publish this data in the agency\u2019s fiscal year budget justification materials, including a comparison of the average login rates of\u00a0on-site and teleworking employees.</p><p>Next, the bill directs any manager who revokes\u00a0a teleworking employee's authorization to telework\u00a0(due to a reason specific to that employee)\u00a0to\u00a0document for the employee and the agency's Human Capital Office\u00a0(1) the total number of days that the employee teleworked in the six work periods immediately preceding the revocation, (2) a narrative summary of the circumstances giving rise to the revocation, and (3) any steps the manager took to discipline the employee before revoking the employee's telework authorization.\u00a0</p><p>Finally, agencies must report to the Chief Human Capital Officers Council\u00a0about any\u00a0adverse effects of telework\u00a0policies\u00a0on the performance of the executive agency. </p>",
      "updateDate": "2025-03-12",
      "versionCode": "id119s21"
    },
    "title": "REMOTE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Requiring Effective Management and Oversight of Teleworking Employees Act or the REMOTE Act</strong></p><p>This bill directs executive agencies to track employees' computer network activity, compare the activity of teleworking and on-site employees,\u00a0and report on any\u00a0deficiencies in the performance of teleworking employees.</p><p>First, the bill requires each agency to establish policies to track for every employee (1) the average number of daily logins,\u00a0(2) the average daily duration of the network connection, and (3) the network traffic generated while the employee works. This information must be collected from employees working primarily on-site within 180 days after the bill's enactment and from teleworking employees within one year after the bill's enactment.\u00a0The bill also directs each agency to publish this data in the agency\u2019s fiscal year budget justification materials, including a comparison of the average login rates of\u00a0on-site and teleworking employees.</p><p>Next, the bill directs any manager who revokes\u00a0a teleworking employee's authorization to telework\u00a0(due to a reason specific to that employee)\u00a0to\u00a0document for the employee and the agency's Human Capital Office\u00a0(1) the total number of days that the employee teleworked in the six work periods immediately preceding the revocation, (2) a narrative summary of the circumstances giving rise to the revocation, and (3) any steps the manager took to discipline the employee before revoking the employee's telework authorization.\u00a0</p><p>Finally, agencies must report to the Chief Human Capital Officers Council\u00a0about any\u00a0adverse effects of telework\u00a0policies\u00a0on the performance of the executive agency. </p>",
      "updateDate": "2025-03-12",
      "versionCode": "id119s21"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s21is.xml"
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
      "title": "REMOTE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REMOTE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-16T01:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Requiring Effective Management and Oversight of Teleworking Employees Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-16T01:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require each Executive department to establish policies and collect information regarding teleworking employees of the Executive department, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-16T01:18:20Z"
    }
  ]
}
```
