# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1563?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1563
- Title: Retired Law Enforcement Officers Continuing Service Act
- Congress: 119
- Bill type: S
- Bill number: 1563
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2025-12-02T12:03:45Z
- Update date including text: 2025-12-02T12:03:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 83.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 83.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1563",
    "number": "1563",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Retired Law Enforcement Officers Continuing Service Act",
    "type": "S",
    "updateDate": "2025-12-02T12:03:45Z",
    "updateDateIncludingText": "2025-12-02T12:03:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 83.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
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
        "item": [
          {
            "date": "2025-05-20T20:18:45Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-15T17:30:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-01T16:37:22Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "IA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "IL"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "HI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "DE"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1563is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1563\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Ms. Klobuchar (for herself and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish a grant program to help law enforcement agencies with civilian law enforcement tasks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Retired Law Enforcement Officers Continuing Service Act .\n#### 2. Grant program\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP Civil law enforcement task grants 3061. Definitions In this part: (1) Civilian law enforcement task The term civilian law enforcement task includes\u2014 (A) assisting in homicide investigations; (B) assisting in carjacking investigations; (C) assisting in financial crimes investigations; (D) reviewing camera footage; (E) crime scene analysis; (F) forensics analysis; and (G) providing expertise in computers, computer networks, information technology, or the internet. (2) Eligible entity The term eligible entity means a State, local, Tribal, or territorial law enforcement agency. 3062. Grants authorized The Attorney General may award grants to eligible entities for the purpose of hiring retired personnel from law enforcement agencies to\u2014 (1) train civilian employees of the eligible entity on civilian law enforcement tasks that can be performed on behalf of a law enforcement agency; and (2) perform civilian law enforcement tasks on behalf of the eligible entity. 3063. Accountability provisions (a) In general A grant awarded under this part shall be subject to the accountability requirements of this section. (b) Audit requirement (1) Definition In this subsection, the term unresolved audit finding means a finding in a final audit report of the Inspector General of the Department of Justice that an audited grantee has used grant funds for an unauthorized expenditure or otherwise unallowable cost that is not closed or resolved within 12 months from the date when the final audit report is issued. (2) Audits Beginning in the first fiscal year beginning after the date of enactment of the Retired Law Enforcement Officers Continuing Service Act , and in each fiscal year thereafter, the Inspector General of the Department of Justice shall conduct audits of recipients of grants under this part to prevent waste, fraud, and abuse of funds by grantees. The Inspector General of the Department of Justice shall determine the appropriate number of grantees to be audited each year. (3) Mandatory exclusion A recipient of grant funds under this part that is found to have an unresolved audit finding shall not be eligible to receive grant funds under this part during the first 2 fiscal years beginning after the end of the 12-month period described in paragraph (1). (4) Priority In awarding grants under this part, the Attorney General shall give priority to eligible entities that did not have an unresolved audit finding during the 3 fiscal years before submitting an application for a grant under this part. (c) Annual certification Beginning in the fiscal year during which audits commence under subsection (b)(2), the Attorney General shall submit to the Committee on the Judiciary and the Committee on Appropriations of the Senate and the Committee on the Judiciary and the Committee on Appropriations of the House of Representatives an annual certification\u2014 (1) indicating whether\u2014 (A) all audits issued by the Office of the Inspector General of the Department of Justice under subsection (b) have been completed and reviewed by the appropriate Assistant Attorney General or Director; and (B) all mandatory exclusions required under subsection (b)(3) have been issued; and (2) that includes a list of any grant recipients excluded under subsection (b)(3) from the previous year. (d) Preventing duplicative grants (1) In general Before the Attorney General awards a grant to an eligible entity under this part, the Attorney General shall compare potential grant awards with other grants awarded by the Attorney General to determine if grant awards are or have been awarded for a similar purpose. (2) Report If the Attorney General awards grants to the same applicant for a similar purpose, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that includes\u2014 (A) a list of all such grants awarded, including the total dollar amount of any such grants awarded; and (B) the reason the Attorney General awarded multiple grants to the same applicant for a similar purpose. .",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1563rs.xml",
      "text": "II\nCalendar No. 83\n119th CONGRESS\n1st Session\nS. 1563\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Ms. Klobuchar (for herself, Mr. Grassley , Mr. Durbin , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 20, 2025 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish a grant program to help law enforcement agencies with civilian law enforcement tasks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Retired Law Enforcement Officers Continuing Service Act .\n#### 2. Grant program\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP Civil law enforcement task grants 3061. Definitions In this part: (1) Civilian law enforcement task The term civilian law enforcement task includes\u2014 (A) assisting in homicide investigations; (B) assisting in carjacking investigations; (C) assisting in financial crimes investigations; (D) reviewing camera footage; (E) crime scene analysis; (F) forensics analysis; and (G) providing expertise in computers, computer networks, information technology, or the internet. (2) Eligible entity The term eligible entity means a State, local, Tribal, or territorial law enforcement agency. 3062. Grants authorized The Attorney General may award grants to eligible entities for the purpose of hiring retired personnel from law enforcement agencies to\u2014 (1) train civilian employees of the eligible entity on civilian law enforcement tasks that can be performed on behalf of a law enforcement agency; and (2) perform civilian law enforcement tasks on behalf of the eligible entity. 3063. Accountability provisions (a) In general A grant awarded under this part shall be subject to the accountability requirements of this section. (b) Audit requirement (1) Definition In this subsection, the term unresolved audit finding means a finding in a final audit report of the Inspector General of the Department of Justice that an audited grantee has used grant funds for an unauthorized expenditure or otherwise unallowable cost that is not closed or resolved within 12 months from the date when the final audit report is issued. (2) Audits Beginning in the first fiscal year beginning after the date of enactment of the Retired Law Enforcement Officers Continuing Service Act , and in each fiscal year thereafter, the Inspector General of the Department of Justice shall conduct audits of recipients of grants under this part to prevent waste, fraud, and abuse of funds by grantees. The Inspector General of the Department of Justice shall determine the appropriate number of grantees to be audited each year. (3) Mandatory exclusion A recipient of grant funds under this part that is found to have an unresolved audit finding shall not be eligible to receive grant funds under this part during the first 2 fiscal years beginning after the end of the 12-month period described in paragraph (1). (4) Priority In awarding grants under this part, the Attorney General shall give priority to eligible entities that did not have an unresolved audit finding during the 3 fiscal years before submitting an application for a grant under this part. (c) Annual certification Beginning in the fiscal year during which audits commence under subsection (b)(2), the Attorney General shall submit to the Committee on the Judiciary and the Committee on Appropriations of the Senate and the Committee on the Judiciary and the Committee on Appropriations of the House of Representatives an annual certification\u2014 (1) indicating whether\u2014 (A) all audits issued by the Office of the Inspector General of the Department of Justice under subsection (b) have been completed and reviewed by the appropriate Assistant Attorney General or Director; and (B) all mandatory exclusions required under subsection (b)(3) have been issued; and (2) that includes a list of any grant recipients excluded under subsection (b)(3) from the previous year. (d) Preventing duplicative grants (1) In general Before the Attorney General awards a grant to an eligible entity under this part, the Attorney General shall compare potential grant awards with other grants awarded by the Attorney General to determine if grant awards are or have been awarded for a similar purpose. (2) Report If the Attorney General awards grants to the same applicant for a similar purpose, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that includes\u2014 (A) a list of all such grants awarded, including the total dollar amount of any such grants awarded; and (B) the reason the Attorney General awarded multiple grants to the same applicant for a similar purpose. .",
      "versionDate": "2025-05-20",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-06-09",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3846",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Retired Law Enforcement Officers Continuing Service Act",
      "type": "HR"
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
            "name": "Accounting and auditing",
            "updateDate": "2025-06-05T14:25:45Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-05T14:25:52Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-06-05T14:25:37Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-05T14:25:28Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-06-05T14:25:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-21T12:28:15Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1563is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1563rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Retired Law Enforcement Officers Continuing Service Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T12:03:45Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Retired Law Enforcement Officers Continuing Service Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Retired Law Enforcement Officers Continuing Service Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T14:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish a grant program to help law enforcement agencies with civilian law enforcement tasks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T14:18:21Z"
    }
  ]
}
```
