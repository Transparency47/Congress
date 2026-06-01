# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/687?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/687
- Title: BCRA of 2025
- Congress: 119
- Bill type: S
- Bill number: 687
- Origin chamber: Senate
- Introduced date: 2025-02-24
- Update date: 2025-12-05T22:50:54Z
- Update date including text: 2025-12-05T22:50:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-24: Introduced in Senate
- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-24: Introduced in Senate

## Actions

- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/687",
    "number": "687",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "BCRA of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:50:54Z",
    "updateDateIncludingText": "2025-12-05T22:50:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T20:51:16Z",
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
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s687is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 687\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2025 Mr. Ossoff (for himself and Mr. Kennedy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo encourage States to report to the Attorney General certain information regarding inmates who give birth in the custody of law enforcement agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Births in Custody Reporting Act of 2025 or the BCRA of 2025 .\n#### 2. State information regarding pregnant individuals and individuals who give birth in the custody of law enforcement\n##### (a) Definitions\nIn this section, the terms boot camp prison and State have the meanings given those terms, respectively, in section 901(a) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251(a) ).\n##### (b) Report\nFor each fiscal year after the expiration of the period specified in subsection (e)(1) in which a State receives funds for a program referred to in subsection (e)(2), the State shall report to the Attorney General, on a quarterly basis and pursuant to guidelines established by the Attorney General, anonymized and aggregate information regarding any inmates who are pregnant or who have given birth while detained or incarcerated at a custodial facility within the jurisdiction of the State, including a municipal or county jail, State prison, State-run boot camp prison, boot camp prison that is contracted out by the State, any State or local contract facility, or other local or State correctional facility (including any juvenile facility).\n##### (c) Information required\nThe report required by subsection (b) shall contain information that, at a minimum, includes\u2014\n**(1)**\nthe total number of pregnant inmates in custody to date in that calendar year;\n**(2)**\nthe race and ethnicity of each pregnant inmate described in paragraph (1);\n**(3)**\nthe quarter of admission to custody for each pregnant inmate described under paragraph (1);\n**(4)**\nwhether each female inmate was administered a pregnancy test not later than 1 week after admission to custody;\n**(5)**\nwhether each pregnant inmate received a prenatal visit with a qualified medical professional not later than 7 days after facility personnel determined that the inmate was pregnant;\n**(6)**\nthe outcome of each inmate\u2019s pregnancy if the pregnancy occurred while the inmate was in custody, including live birth, stillbirth, miscarriage, ectopic pregnancy, maternal death, neonatal death, and preterm birth;\n**(7)**\nthe quarter when the pregnant inmate was released from custody or when the pregnancy outcome described in paragraph (6) occurred, whichever occurs first;\n**(8)**\nwhether each outcome under paragraph (6) took place at the custodial facility or at an off-site location, and if at an off-site location, which off-site location;\n**(9)**\nthe number of times that restraints were used on each pregnant inmate, the type of restraint used, and the justification for the use of restraints, and including the following information\u2014\n**(A)**\nwhether restraints were used during pregnancy, during labor, or during delivery;\n**(B)**\nwhether restraints were used while the pregnant inmate was in transit between the custodial facility and medical appointments, a hospital, or court proceedings; and\n**(C)**\nwhether restraints were used on the pregnant inmate\u2019s ankles, wrists, or abdomen;\n**(10)**\nthe number of pregnant inmates who were still in custody postpartum, defined as at least 12 weeks after delivery, and information about each of those inmates, including\u2014\n**(A)**\nwhether each inmate, as described in this paragraph, received a screening for postpartum depression with a qualified medical provider; and\n**(B)**\nwhether each inmate, as described in this paragraph, received a postpartum medical appointment with a qualified medical provider not later than 2 weeks after delivery; and\n**(11)**\nthe total number of inmates described in paragraphs (1) and (10) who were placed in restrictive housing while pregnant or postpartum, the reason for such placement, and the amount of time spent in restrictive housing.\n##### (d) Personally identifiable information\nData collected under subsection (c) may not contain any personally identifiable information of any incarcerated pregnant or postpartum inmate.\n##### (e) Compliance and ineligibility\n**(1) Compliance date**\nEach State shall have not more than 120 days from the date of enactment of this Act to comply with subsection (b), except that the Attorney General may grant an additional 120 days to a State that is making good faith efforts to comply with such subsection.\n**(2) Ineligibility for funds**\nFor any fiscal year after the expiration of the period specified in paragraph (1), a State that fails to comply with subsection (b), shall, at the discretion of the Attorney General, be subject to not more than a 10-percent reduction of the funds that would otherwise be allocated for that fiscal year to the State under subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ).\n##### (f) Reallocation\nAmounts not allocated under the program referred to in subsection (e)(2) to a State for failure to fully comply with subsection (b) shall be reallocated under that program to States that have not failed to comply with such subsection.\n##### (g) Publication of reports by Attorney General\nThe Attorney General shall make available to the public each report submitted under subsection (b).\n##### (h) Study required\nThe Attorney General shall carry out a study on the information reported under subsection (c) to\u2014\n**(1)**\ndetermine means by which such information can be used to improve the treatment of inmates who are pregnant or who have given birth at the jails, prisons, and other specified facilities covered in the reports; and\n**(2)**\nexamine\u2014\n**(A)**\nthe relationship, if any, between stillbirths, miscarriages, maternal deaths, neonatal deaths, and preterm births that occur while inmates are in custody; and\n**(B)**\nthe actions of management of such jails, prisons, and other specified facilities.\n##### (i) Report to Congress\nNot later than 2 years after the date of enactment of this Act, the Attorney General shall prepare and submit to Congress a report that contains the findings of the study required by subsection (h).",
      "versionDate": "2025-02-24",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-10-31",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5901",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BCRA of 2025",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-17T20:26:29Z"
          },
          {
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-07-17T20:26:01Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-17T20:25:37Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-17T20:26:22Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-07-17T20:26:11Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-07-17T20:26:05Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-07-17T20:26:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-21T16:06:29Z"
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
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s687is.xml"
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
      "title": "BCRA of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BCRA of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Births in Custody Reporting Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to encourage States to report to the Attorney General certain information regarding inmates who give birth in the custody of law enforcement agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:47Z"
    }
  ]
}
```
