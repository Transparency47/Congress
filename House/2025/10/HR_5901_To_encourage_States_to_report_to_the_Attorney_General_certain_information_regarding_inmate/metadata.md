# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5901?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5901
- Title: BCRA of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5901
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2025-12-05T22:52:39Z
- Update date including text: 2025-12-05T22:52:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5901",
    "number": "5901",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000808",
        "district": "24",
        "firstName": "Frederica",
        "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
        "lastName": "Wilson",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "BCRA of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:52:39Z",
    "updateDateIncludingText": "2025-12-05T22:52:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
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
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:03:40Z",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "DC"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "GA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "GA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MO"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "PA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "AL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MS"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "DE"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "OR"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5901ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5901\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Ms. Wilson of Florida (for herself, Mr. Van Drew , Ms. Norton , Mr. Bishop , Mr. Johnson of Georgia , Ms. Crockett , Mr. Cleaver , Ms. Lee of Pennsylvania , Ms. Sewell , Mr. Thompson of Mississippi , Ms. McBride , Ms. Clarke of New York , Ms. Salinas , and Mr. David Scott of Georgia ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo encourage States to report to the Attorney General certain information regarding inmates who give birth in the custody of law enforcement agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Births in Custody Reporting Act of 2025 or the BCRA of 2025 .\n#### 2. State information regarding pregnant individuals and individuals who give birth in the custody of law enforcement\n##### (a) Definitions\nIn this section, the terms boot camp prison and State have the meanings given those terms, respectively, in section 901(a) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251(a) ).\n##### (b) Report\nFor each fiscal year after the expiration of the period specified in subsection (e)(1) in which a State receives funds for a program referred to in subsection (e)(2), the State shall report to the Attorney General, on a quarterly basis and pursuant to guidelines established by the Attorney General, anonymized and aggregate information regarding any inmates who are pregnant or who have given birth while detained or incarcerated at a custodial facility within the jurisdiction of the State, including a municipal or county jail, State prison, State-run boot camp prison, boot camp prison that is contracted out by the State, any State or local contract facility, or other local or State correctional facility (including any juvenile facility).\n##### (c) Information required\nThe report required by subsection (b) shall contain information that, at a minimum, includes\u2014\n**(1)**\nthe total number of pregnant inmates in custody to date in that calendar year;\n**(2)**\nthe race and ethnicity of each pregnant inmate described in paragraph (1);\n**(3)**\nthe quarter of admission to custody for each pregnant inmate described under paragraph (1);\n**(4)**\nwhether each female inmate was administered a pregnancy test not later than 1 week after admission to custody;\n**(5)**\nwhether each pregnant inmate received a prenatal visit with a qualified medical professional not later than 7 days after facility personnel determined that the inmate was pregnant;\n**(6)**\nthe outcome of each inmate\u2019s pregnancy if the pregnancy occurred while the inmate was in custody, including live birth, stillbirth, miscarriage, ectopic pregnancy, maternal death, neonatal death, and preterm birth;\n**(7)**\nthe quarter when the pregnant inmate was released from custody or when the pregnancy outcome described in paragraph (6) occurred, whichever occurs first;\n**(8)**\nwhether each outcome under paragraph (6) took place at the custodial facility or at an off-site location, and if at an off-site location, which off-site location;\n**(9)**\nthe number of times that restraints were used on each pregnant inmate, the type of restraint used, and the justification for the use of restraints, and including the following information\u2014\n**(A)**\nwhether restraints were used during pregnancy, during labor, or during delivery;\n**(B)**\nwhether restraints were used while the pregnant inmate was in transit between the custodial facility and medical appointments, a hospital, or court proceedings; and\n**(C)**\nwhether restraints were used on the pregnant inmate\u2019s ankles, wrists, or abdomen;\n**(10)**\nthe number of pregnant inmates who were still in custody postpartum, defined as at least 12 weeks after delivery, and information about each of those inmates, including\u2014\n**(A)**\nwhether each inmate, as described in this paragraph, received a screening for postpartum depression with a qualified medical provider; and\n**(B)**\nwhether each inmate, as described in this paragraph, received a postpartum medical appointment with a qualified medical provider not later than 2 weeks after delivery; and\n**(11)**\nthe total number of inmates described in paragraphs (1) and (10) who were placed in restrictive housing while pregnant or postpartum, the reason for such placement, and the amount of time spent in restrictive housing.\n##### (d) Personally identifiable information\nData collected under subsection (c) may not contain any personally identifiable information of any incarcerated pregnant or postpartum inmate.\n##### (e) Compliance and ineligibility\n**(1) Compliance date**\nEach State shall have not more than 120 days from the date of enactment of this Act to comply with subsection (b), except that the Attorney General may grant an additional 120 days to a State that is making good faith efforts to comply with such subsection.\n**(2) Ineligibility for funds**\nFor any fiscal year after the expiration of the period specified in paragraph (1), a State that fails to comply with subsection (b), shall, at the discretion of the Attorney General, be subject to not more than a 10-percent reduction of the funds that would otherwise be allocated for that fiscal year to the State under subpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ).\n##### (f) Reallocation\nAmounts not allocated under the program referred to in subsection (e)(2) to a State for failure to fully comply with subsection (b) shall be reallocated under that program to States that have not failed to comply with such subsection.\n##### (g) Publication of reports by Attorney General\nThe Attorney General shall make available to the public each report submitted under subsection (b).\n##### (h) Study required\nThe Attorney General shall carry out a study on the information reported under subsection (c) to\u2014\n**(1)**\ndetermine means by which such information can be used to improve the treatment of inmates who are pregnant or who have given birth at the jails, prisons, and other specified facilities covered in the reports; and\n**(2)**\nexamine\u2014\n**(A)**\nthe relationship, if any, between stillbirths, miscarriages, maternal deaths, neonatal deaths, and preterm births that occur while inmates are in custody; and\n**(B)**\nthe actions of management of such jails, prisons, and other specified facilities.\n##### (i) Report to Congress\nNot later than 2 years after the date of enactment of this Act, the Attorney General shall prepare and submit to Congress a report that contains the findings of the study required by subsection (h).",
      "versionDate": "2025-10-31",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-02-24",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "687",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BCRA of 2025",
      "type": "S"
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
        "updateDate": "2025-11-19T12:48:35Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5901ih.xml"
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
      "title": "BCRA of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BCRA of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Births in Custody Reporting Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To encourage States to report to the Attorney General certain information regarding inmates who give birth in the custody of law enforcement agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T09:48:15Z"
    }
  ]
}
```
