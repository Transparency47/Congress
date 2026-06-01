# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1098?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1098
- Title: Opioid Overdose Data Collection Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 1098
- Origin chamber: Senate
- Introduced date: 2025-03-24
- Update date: 2026-04-09T15:36:31Z
- Update date including text: 2026-04-09T15:36:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-24: Introduced in Senate
- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-07-24 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-07-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 127.
- Latest action: 2025-03-24: Introduced in Senate

## Actions

- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-07-24 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-07-28 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-07-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 127.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1098",
    "number": "1098",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Opioid Overdose Data Collection Enhancement Act",
    "type": "S",
    "updateDate": "2026-04-09T15:36:31Z",
    "updateDateIncludingText": "2026-04-09T15:36:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 127.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-07-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-07-28",
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
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-24",
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
      "actionDate": "2025-03-24",
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
            "date": "2025-07-28T19:59:30Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-24T14:07:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-24T22:55:52Z",
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
      "sponsorshipDate": "2025-03-24",
      "state": "IA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MN"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "CT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "DE"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "AZ"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1098is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1098\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Ms. Cantwell (for herself, Mr. Grassley , Ms. Klobuchar , and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to enhance the Comprehensive Opioid Abuse Grant Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Opioid Overdose Data Collection Enhancement Act .\n#### 2. Purpose\nThe purpose of this Act is to expand the adoption and implementation of, and provide interoperability of, data collection tools used to track fatal and nonfatal overdoses and opioid overdose reversal medication administration in near real-time through a web-based, mobile-friendly software platform.\n#### 3. Comprehensive opioid abuse grant program\nSection 3021 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10701 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin subparagraph (G), by striking ; and at the end;\n**(B)**\nin subparagraph (H), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(I) an overdose data collection program described in subsection (g)(1). ; and\n**(2)**\nby adding at the end the following:\n(g) Overdose data collection program (1) In general An overdose data collection program described in this paragraph is a program under which a State, unit of local government, coalition of law enforcement agencies, or Indian tribe develops and implements a data collection tool, including mobile data mapping applications, with which the State, unit of local government, coalition of law enforcement agencies, or Indian tribe can easily and quickly track the locations of\u2014 (A) suspected fatal and nonfatal overdoses; and (B) the administration of opioid overdose reversal medication by first responders, including law enforcement officers, firefighters, and emergency medical service technicians. (2) Eligibility of coalitions (A) In general Notwithstanding subsection (a)(1), a coalition of law enforcement agencies shall be eligible to receive a grant under subsection (a) only for the purpose of implementing an overdose data collection program described in paragraph (1) of this subsection. (B) Requirements A coalition of law enforcement agencies seeking a grant under subsection (a) to implement an overdose data collection program described in paragraph (1) of this subsection shall be subject to the same requirements and authorizations to which a States, units of local government, and Indian tribes are subject under this section, including the requirement to submit an application under section 3022. (3) Requirements A State, unit of local government, coalition of law enforcement agencies, or Indian tribe implementing an overdose data collection program described in paragraph (1) shall\u2014 (A) support the development of coordinated public safety, behavioral health, and public health responses to the data collected by the tool described in paragraph (1); (B) focus on areas in which fatal and nonfatal overdoses occur and trends of concern; (C) provide for interoperability with existing Federal, State, local, and Tribal overdose data collection tools and overdose data collection tools of coalitions of law enforcement agencies; and (D) make data collected through the program available to Federal, State, Tribal, and territorial governments and coalitions of law enforcement agencies. (4) Audit; application A State, unit of local government, coalition of law enforcement agencies, or Indian tribe seeking to use a grant received under subsection (a) for a program described in paragraph (1) of this subsection shall\u2014 (A) conduct an audit of available data and resources; and (B) in order to avoid duplication, submit the audit conducted under subparagraph (A) as a part of the application for the grant of the State, unit of local government, coalition of law enforcement agencies, or Indian tribe. (5) Consultation In carrying out this subsection, the Attorney General shall consult with the heads of agencies that maintain overdose data collection tools, including the Director of the Office of National Drug Control Policy. .",
      "versionDate": "2025-03-24",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1098rs.xml",
      "text": "II\nCalendar No. 127\n119th CONGRESS\n1st Session\nS. 1098\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Ms. Cantwell (for herself, Mr. Grassley , Ms. Klobuchar , Mr. Cornyn , Mr. Blumenthal , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nJuly 28, 2025 Reported by Mr. Grassley , with an amendment Omit the part struck through\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to enhance the Comprehensive Opioid Abuse Grant Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Opioid Overdose Data Collection Enhancement Act .\n#### 2. Purpose\nThe purpose of this Act is to expand the adoption and implementation of, and provide interoperability of, data collection tools used to track fatal and nonfatal overdoses and opioid overdose reversal medication administration in near real-time through a web-based, mobile-friendly software platform.\n#### 3. Comprehensive opioid abuse grant program\nSection 3021 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10701 ) is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nin subparagraph (G), by striking ; and at the end;\n**(B)**\nin subparagraph (H), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(I) an overdose data collection program described in subsection (g)(1). ; and\n**(2)**\nby adding at the end the following:\n(g) Overdose data collection program (1) In general An overdose data collection program described in this paragraph is a program under which a State, unit of local government, coalition of law enforcement agencies, or Indian tribe develops and implements a data collection tool, including mobile data mapping applications, with which the State, unit of local government, coalition of law enforcement agencies, or Indian tribe can easily and quickly track the locations of\u2014 (A) suspected fatal and nonfatal overdoses; and (B) the administration of opioid overdose reversal medication by first responders, including law enforcement officers, firefighters, and emergency medical service technicians. (2) Eligibility of coalitions (A) In general Notwithstanding subsection (a)(1), a coalition of law enforcement agencies shall be eligible to receive a grant under subsection (a) only for the purpose of implementing an overdose data collection program described in paragraph (1) of this subsection. (B) Requirements A coalition of law enforcement agencies seeking a grant under subsection (a) to implement an overdose data collection program described in paragraph (1) of this subsection shall be subject to the same requirements and authorizations to which a States, units of local government, and Indian tribes are subject under this section, including the requirement to submit an application under section 3022. (3) Requirements A State, unit of local government, coalition of law enforcement agencies, or Indian tribe implementing an overdose data collection program described in paragraph (1) shall\u2014 (A) support the development of coordinated public safety, behavioral health, and public health responses to the data collected by the tool described in paragraph (1); (B) focus on areas in which fatal and nonfatal overdoses occur and trends of concern; (C) provide for interoperability with existing Federal, State, local, and Tribal overdose data collection tools and overdose data collection tools of coalitions of law enforcement agencies; and (D) make data collected through the program available to Federal, State, Tribal, and territorial governments and coalitions of law enforcement agencies. (4) Audit; application A State, unit of local government, coalition of law enforcement agencies, or Indian tribe seeking to use a grant received under subsection (a) for a program described in paragraph (1) of this subsection shall\u2014 (A) conduct an audit of available data and resources; and (B) in order to avoid duplication, submit the audit conducted under subparagraph (A) as a part of the application for the grant of the State, unit of local government, coalition of law enforcement agencies, or Indian tribe. (5) Consultation In carrying out this subsection, the Attorney General shall consult with the heads of agencies that maintain overdose data collection tools, including the Director of the Office of National Drug Control Policy. .",
      "versionDate": "2025-07-28",
      "versionType": "Reported in Senate"
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
            "updateDate": "2025-08-07T17:53:28Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-09T15:36:31Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-08-07T17:53:28Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-08-07T17:53:28Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-08-07T17:53:28Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-08-07T17:53:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-04-10T15:35:53Z"
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
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1098is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-07-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1098rs.xml"
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
      "title": "Opioid Overdose Data Collection Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-24T11:03:15Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Opioid Overdose Data Collection Enhancement Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Opioid Overdose Data Collection Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to enhance the Comprehensive Opioid Abuse Grant Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:33:25Z"
    }
  ]
}
```
