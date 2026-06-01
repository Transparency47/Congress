# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7733?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7733
- Title: Ensuring OB–GYN Care in Prisons Act
- Congress: 119
- Bill type: HR
- Bill number: 7733
- Origin chamber: House
- Introduced date: 2026-02-26
- Update date: 2026-05-21T08:07:35Z
- Update date including text: 2026-05-21T08:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-26: Introduced in House

## Actions

- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Introduced in House
- 2026-02-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7733",
    "number": "7733",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "F000477",
        "district": "4",
        "firstName": "Valerie",
        "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
        "lastName": "Foushee",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Ensuring OB\u2013GYN Care in Prisons Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:35Z",
    "updateDateIncludingText": "2026-05-21T08:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-26",
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
      "actionDate": "2026-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T14:32:05Z",
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
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "AZ"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "CA"
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
      "sponsorshipDate": "2026-02-26",
      "state": "GA"
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
      "sponsorshipDate": "2026-02-26",
      "state": "DC"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "WA"
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
      "sponsorshipDate": "2026-02-26",
      "state": "PA"
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
      "sponsorshipDate": "2026-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MI"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "IL"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MI"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "FL"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NC"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NM"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7733ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7733\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2026 Mrs. Foushee (for herself, Ms. Ansari , Ms. Kamlager-Dove , Mr. Johnson of Georgia , Ms. Norton , Mrs. McIver , Mr. Veasey , Mr. Evans of Pennsylvania , Ms. Randall , Ms. Lee of Pennsylvania , and Mr. Goldman of New York ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to ensure access to obstetrician-gynecologists for female prisoners, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring OB\u2013GYN Care in Prisons Act .\n#### 2. Employment of obstetrician-gynecologists at Bureau of Prisons facilities\nSection 4051(h)(3) of title 18, United States Code, is amended to read as follows:\n(3) Obstetrician-gynecologist access (A) In general The Director shall ensure that all prisoners have access to an obstetrician-gynecologist in accordance with this paragraph, and shall employ at least one (and may employ more than one) obstetrician-gynecologist certified by the American Board of Obstetrics and Gynecology on a full-time basis at each facility of the Bureau of Prisons at which female prisoners are incarcerated (B) Initial visit The Director shall ensure that each female prisoner incarcerated by the Bureau of Prisons has an initial visit with the obstetrician-gynecologist employed at the facility at which the prisoner is incarcerated not later than 14 days after imprisonment. (C) Services An obstetrician-gynecologist employed under this paragraph shall provide female prisoners with the following services: (i) Menstrual health care and pain management. (ii) Contraceptive counseling and access. (iii) Diagnosis and treatment of gynecological conditions. (iv) Cancer screenings consistent with clinical guidelines. (v) Prenatal care and pregnancy screenings. (vi) Postpartum care and recovery. (vii) Mental health screening for postpartum depression. (D) Protections for prisoners With respect to services provided by obstetrician-gynecologists, female prisoners shall be provided the following: (i) Informed consent for any exam or procedure. (ii) The right to refuse non-emergency care. (iii) Clear communication in the preferred language of the prisoner. (E) Standards In providing services under this paragraph, the obstetrician-gynecologist shall use of trauma-informed care standards for survivors of sexual violence. (F) Referrals The Director\u2014 (i) shall establish a process for female prisoners to receive referrals to and care from other medical specialists when medically necessary, as determined by the obstetrician-gynecologist; (ii) shall ensure that transportation and security arrangements do not delay a prisoner\u2019s access to such care; and (iii) may not deny providing a prisoner with such care based on cost or staffing constraints. (G) Vacancies The Director shall fill any vacancy in an obstetrician-gynecologist position required under this paragraph not later than 42 days after such vacancy is created. .\n#### 3. Report\nNot later than one year after the date of enactment of this Act, and on an annual basis thereafter, the Director of the Bureau of Prisons shall submit to Congress a report that includes the following:\n**(1)**\nThe name of each facility of the Bureau of Prisons at which at least one obstetrician-gynecologist is employed on a full-time basis.\n**(2)**\nThe name of each facility of the Bureau of Prisons at which the employment of at least one obstetrician-gynecologist is required under section 4051(h)(3) of title 18, United States Code, which position is vacant, and the duration of such vacancy.\n**(3)**\nDuring the previous one-year period, for each facility of the Bureau of Prisons at which female prisoners are incarcerated, the number of\u2014\n**(A)**\nvisits to an obstetrician-gynecologist employed at the facility in accordance with section 4051(h)(3) of title 18, United States Code, by\u2014\n**(i)**\nfemale prisoners; and\n**(ii)**\npregnant prisoners;\n**(B)**\nthe number of hours worked by each such obstetrician-gynecologist at such facility;\n**(C)**\nchildbirths by prisoners;\n**(D)**\npregnancies of prisoners that were classified as high-risk by an obstetrician-gynecologist described in subparagraph (C), and any pregnancies that were so classified by any other obstetrician-gynecologist; and\n**(E)**\ndeaths of\u2014\n**(i)**\nfemale prisoners related to pregnancy; and\n**(ii)**\nnewborn children of pregnant prisoners.",
      "versionDate": "2026-02-26",
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
        "updateDate": "2026-03-04T15:50:12Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7733ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring OB\u2013GYN Care in Prisons Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-03T06:23:21Z"
    },
    {
      "title": "Ensuring OB\u2013GYN Care in Prisons Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to ensure access to obstetrician-gynecologists for female prisoners, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-03T06:18:25Z"
    }
  ]
}
```
