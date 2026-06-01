# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/307?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/307
- Title: Prison Staff Safety Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 307
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2026-04-09T15:41:22Z
- Update date including text: 2026-04-09T15:41:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-29 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2643; text: CR S2643)
- 2025-04-29 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2643: 2; text: CR S2643)
- 2025-04-29 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-04-29 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-05-01 - Floor: Message on Senate action sent to the House.
- 2025-05-05 14:08:45 - Floor: Received in the House.
- 2025-05-05 14:28:27 - Floor: Held at the desk.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-04-29 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2643; text: CR S2643)
- 2025-04-29 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2643: 2; text: CR S2643)
- 2025-04-29 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-04-29 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-05-01 - Floor: Message on Senate action sent to the House.
- 2025-05-05 14:08:45 - Floor: Received in the House.
- 2025-05-05 14:28:27 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/307",
    "number": "307",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Prison Staff Safety Enhancement Act",
    "type": "S",
    "updateDate": "2026-04-09T15:41:22Z",
    "updateDateIncludingText": "2026-04-09T15:41:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-05-05",
      "actionTime": "14:28:27",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-05-05",
      "actionTime": "14:08:45",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S2643; text: CR S2643)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2643: 2; text: CR S2643)",
      "type": "Floor"
    },
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-04-29",
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
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
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
      "actionDate": "2025-01-29",
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
            "date": "2025-04-30T01:25:34Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-01-29T19:39:15Z",
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
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "GA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-19",
      "state": "WV"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s307is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 307\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mrs. Blackburn (for herself and Mr. Ossoff ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo address sexual harassment and sexual assault of Bureau of Prisons staff in prisons, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prison Staff Safety Enhancement Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 2023, the Office of the Inspector General of the Department of Justice released a report titled Evaluation of the Federal Bureau of Prisons\u2019 Efforts to Address Sexual Harassment and Sexual Assault Committed by Inmates Toward Staff (in this section referred to as the Inspector General report ).\n**(2)**\nThe Inspector General report examined all sanctioned inmate sexual incidents in the Bureau of Prisons (in this section referred to as the Bureau ) between fiscal years 2015 and 2021, and found that inmate-on-staff sexual harassment and sexual assault is widespread.\n**(3)**\nThe Inspector General report further found that the Bureau does not collect adequate data on inmate-on-staff sexual harassment and sexual assault and that, because of the Bureau's inadequate data, the Bureau has not been able to identify the full scope of inmate-on-staff sexual harassment and sexual assault.\n**(4)**\nThe Inspector General report further found that the Bureau does not have systems to evaluate the effectiveness of the Bureau's strategies to mitigate inmate-on-staff sexual harassment and sexual assault.\n**(5)**\nThe Inspector General report made recommendations to the Bureau to address the failures in the Bureau's data collection and mitigation efforts, but the Bureau has not implemented these recommendations.\n#### 3. Addressing sexual harassment and sexual assault of Bureau of Prisons staff\n##### (a) Definitions\nIn this section:\n**(1) Bureau**\nThe term Bureau means the Bureau of Prisons.\n**(2) Correctional officer**\nThe term correctional officer has the meaning given the term in section 4051 of title 18, United States Code.\n**(3) Inspector General**\nThe term Inspector General means the Inspector General of the Department of Justice.\n**(4) Incarcerated individual**\nThe term incarcerated individual has the meaning given the term prisoner in section 4051 of title 18, United States Code.\n**(5) Sexual assault**\nThe term sexual assault means an act described in subsection (b), (c), or (d) of section 920 of title 10, United States Code.\n**(6) Sexual harassment**\nThe term sexual harassment means unwelcome sexual advances, requests for sexual favors, or other verbal or physical conduct of a sexual nature that explicitly or implicitly affect an individual\u2019s employment, unreasonably interfere with an individual\u2019s work performance, or create an intimidating, hostile, or offensive work environment.\n##### (b) Implementation of recommendations by Bureau\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Bureau shall fully implement each recommendation in the report released by the Inspector General in 2023 titled Evaluation of the Federal Bureau of Prisons\u2019 Efforts to Address Sexual Harassment and Sexual Assault Committed by Inmates Toward Staff .\n**(2) Report**\nIf the Bureau has not fully implemented each recommendation referenced in paragraph (1) by the deadline under that paragraph, the Bureau shall submit a report to Congress by that deadline that includes an explanation of the failure to fully implement each recommendation and a detailed timeline for full implementation.\n##### (c) Data analysis by Inspector General\n**(1) In general**\nNot later than 1 year after the date as of which the Bureau has fully implemented each recommendation referenced in subsection (b)(1)\u2014\n**(A)**\nthe Inspector General shall request from the Bureau, and the Bureau shall provide, updated data on the number and prevalence of sexual harassment and sexual assault incidents perpetrated by incarcerated individuals against a correctional officer or other employee of the Bureau during fiscal years 2022 through 2025;\n**(B)**\nthe Inspector General shall conduct an analysis of the data described in subparagraph (A); and\n**(C)**\nthe Inspector General shall provide Congress and the Attorney General with the analysis conducted under subparagraph (B) and any additional recommendations, including analysis of whether the Bureau has taken sufficient steps to identify the prevalence and scope of sexual harassment and sexual assault incidents perpetrated by incarcerated individuals against a correctional officer or other employee of the Bureau and to mitigate such incidents.\n**(2) Analysis of punishments**\nThe analysis required under paragraph (1)(C) shall include an analysis of punishments for sexual harassment and sexual assault as of the date of enactment of this Act in facilities controlled by the Bureau of Prisons, including data on the use of such punishments during the 5-year period preceding the date of enactment of this Act.\n##### (d) Rulemaking by Attorney General\nNot later than 1 year after receiving the analysis under subsection (c), the Attorney General shall promulgate a rule adopting national standards for prevention, reduction, and punishment of sexual harassment and sexual assault perpetrated by an incarcerated individual against a correctional officer or other employee of the Bureau.",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s307es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 307\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo address sexual harassment and sexual assault of Bureau of Prisons staff in prisons, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prison Staff Safety Enhancement Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 2023, the Office of the Inspector General of the Department of Justice released a report titled Evaluation of the Federal Bureau of Prisons\u2019 Efforts to Address Sexual Harassment and Sexual Assault Committed by Inmates Toward Staff (in this section referred to as the Inspector General report ).\n**(2)**\nThe Inspector General report examined all sanctioned inmate sexual incidents in the Bureau of Prisons (in this section referred to as the Bureau ) between fiscal years 2015 and 2021, and found that inmate-on-staff sexual harassment and sexual assault is widespread.\n**(3)**\nThe Inspector General report further found that the Bureau does not collect adequate data on inmate-on-staff sexual harassment and sexual assault and that, because of the Bureau's inadequate data, the Bureau has not been able to identify the full scope of inmate-on-staff sexual harassment and sexual assault.\n**(4)**\nThe Inspector General report further found that the Bureau does not have systems to evaluate the effectiveness of the Bureau's strategies to mitigate inmate-on-staff sexual harassment and sexual assault.\n**(5)**\nThe Inspector General report made recommendations to the Bureau to address the failures in the Bureau's data collection and mitigation efforts, but the Bureau has not implemented these recommendations.\n#### 3. Addressing sexual harassment and sexual assault of Bureau of Prisons staff\n##### (a) Definitions\nIn this section:\n**(1) Bureau**\nThe term Bureau means the Bureau of Prisons.\n**(2) Correctional officer**\nThe term correctional officer has the meaning given the term in section 4051 of title 18, United States Code.\n**(3) Inspector General**\nThe term Inspector General means the Inspector General of the Department of Justice.\n**(4) Incarcerated individual**\nThe term incarcerated individual has the meaning given the term prisoner in section 4051 of title 18, United States Code.\n**(5) Sexual assault**\nThe term sexual assault means an act described in subsection (b), (c), or (d) of section 920 of title 10, United States Code.\n**(6) Sexual harassment**\nThe term sexual harassment means unwelcome sexual advances, requests for sexual favors, or other verbal or physical conduct of a sexual nature that explicitly or implicitly affect an individual\u2019s employment, unreasonably interfere with an individual\u2019s work performance, or create an intimidating, hostile, or offensive work environment.\n##### (b) Implementation of recommendations by Bureau\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Bureau shall fully implement each recommendation in the report released by the Inspector General in 2023 titled Evaluation of the Federal Bureau of Prisons\u2019 Efforts to Address Sexual Harassment and Sexual Assault Committed by Inmates Toward Staff .\n**(2) Report**\nIf the Bureau has not fully implemented each recommendation referenced in paragraph (1) by the deadline under that paragraph, the Bureau shall submit a report to Congress by that deadline that includes an explanation of the failure to fully implement each recommendation and a detailed timeline for full implementation.\n##### (c) Data analysis by Inspector General\n**(1) In general**\nNot later than 1 year after the date as of which the Bureau has fully implemented each recommendation referenced in subsection (b)(1)\u2014\n**(A)**\nthe Inspector General shall request from the Bureau, and the Bureau shall provide, updated data on the number and prevalence of sexual harassment and sexual assault incidents perpetrated by incarcerated individuals against a correctional officer or other employee of the Bureau during fiscal years 2022 through 2025;\n**(B)**\nthe Inspector General shall conduct an analysis of the data described in subparagraph (A); and\n**(C)**\nthe Inspector General shall provide Congress and the Attorney General with the analysis conducted under subparagraph (B) and any additional recommendations, including analysis of whether the Bureau has taken sufficient steps to identify the prevalence and scope of sexual harassment and sexual assault incidents perpetrated by incarcerated individuals against a correctional officer or other employee of the Bureau and to mitigate such incidents.\n**(2) Analysis of punishments**\nThe analysis required under paragraph (1)(C) shall include an analysis of punishments for sexual harassment and sexual assault as of the date of enactment of this Act in facilities controlled by the Bureau of Prisons, including data on the use of such punishments during the 5-year period preceding the date of enactment of this Act.\n##### (d) Rulemaking by Attorney General\nNot later than 1 year after receiving the analysis under subsection (c), the Attorney General shall promulgate a rule adopting national standards for prevention, reduction, and punishment of sexual harassment and sexual assault perpetrated by an incarcerated individual against a correctional officer or other employee of the Bureau.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-04-01T15:21:11Z"
          },
          {
            "name": "Assault and harassment offenses",
            "updateDate": "2025-04-01T15:21:11Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-01T15:21:11Z"
          },
          {
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-04-01T15:21:11Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-09T15:41:21Z"
          },
          {
            "name": "Department of Justice",
            "updateDate": "2025-04-01T15:21:11Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-04-01T15:21:11Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-01T15:21:11Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-04-01T15:21:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-03T21:02:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s307",
          "measure-number": "307",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-09-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s307v00",
            "update-date": "2025-09-16"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Prison Staff Safety Enhancement Act</strong></p><p>This bill establishes requirements for the Department of Justice (DOJ) and component agencies to assess and respond to incidents of sexual harassment and sexual assault by incarcerated individuals against Bureau of Prisons (BOP) staff.</p><p>Specifically, the\u00a0bill requires DOJ\u00a0to adopt national standards for the prevention, reduction, and punishment of sexual harassment and sexual assault by incarcerated individuals against correctional officers or other employees of the BOP.</p><p>Additionally, the bill requires the BOP to fully implement the recommendations of the DOJ Inspector General\u00a0contained in the report titled <em>Evaluation of the Federal Bureau of Prisons\u2019 Efforts to Address Sexual Harassment and Sexual Assault Committed by Inmates Toward Staff</em>.</p>"
        },
        "title": "Prison Staff Safety Enhancement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s307.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prison Staff Safety Enhancement Act</strong></p><p>This bill establishes requirements for the Department of Justice (DOJ) and component agencies to assess and respond to incidents of sexual harassment and sexual assault by incarcerated individuals against Bureau of Prisons (BOP) staff.</p><p>Specifically, the\u00a0bill requires DOJ\u00a0to adopt national standards for the prevention, reduction, and punishment of sexual harassment and sexual assault by incarcerated individuals against correctional officers or other employees of the BOP.</p><p>Additionally, the bill requires the BOP to fully implement the recommendations of the DOJ Inspector General\u00a0contained in the report titled <em>Evaluation of the Federal Bureau of Prisons\u2019 Efforts to Address Sexual Harassment and Sexual Assault Committed by Inmates Toward Staff</em>.</p>",
      "updateDate": "2025-09-16",
      "versionCode": "id119s307"
    },
    "title": "Prison Staff Safety Enhancement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prison Staff Safety Enhancement Act</strong></p><p>This bill establishes requirements for the Department of Justice (DOJ) and component agencies to assess and respond to incidents of sexual harassment and sexual assault by incarcerated individuals against Bureau of Prisons (BOP) staff.</p><p>Specifically, the\u00a0bill requires DOJ\u00a0to adopt national standards for the prevention, reduction, and punishment of sexual harassment and sexual assault by incarcerated individuals against correctional officers or other employees of the BOP.</p><p>Additionally, the bill requires the BOP to fully implement the recommendations of the DOJ Inspector General\u00a0contained in the report titled <em>Evaluation of the Federal Bureau of Prisons\u2019 Efforts to Address Sexual Harassment and Sexual Assault Committed by Inmates Toward Staff</em>.</p>",
      "updateDate": "2025-09-16",
      "versionCode": "id119s307"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s307is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s307es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Prison Staff Safety Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T11:03:16Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Prison Staff Safety Enhancement Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-04-30T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prison Staff Safety Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address sexual harassment and sexual assault of Bureau of Prisons staff in prisons, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:33:23Z"
    }
  ]
}
```
