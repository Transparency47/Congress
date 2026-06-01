# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1295?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1295
- Title: BOP SCAN Mail Act
- Congress: 119
- Bill type: S
- Bill number: 1295
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2025-12-06T07:05:24Z
- Update date including text: 2025-12-06T07:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S2181)
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S2181)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1295",
    "number": "1295",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "J000312",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Justice, James C. [R-WV]",
        "lastName": "Justice",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "BOP SCAN Mail Act",
    "type": "S",
    "updateDate": "2025-12-06T07:05:24Z",
    "updateDateIncludingText": "2025-12-06T07:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S2181)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T20:07:44Z",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "PA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "TN"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "LA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "WV"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "TX"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NH"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "MT"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "OH"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "ID"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "PA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1295is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1295\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mr. Justice (for himself, Mr. Fetterman , Mrs. Blackburn , Mr. Cassidy , Mrs. Capito , Mr. Cruz , and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Director of the Bureau of Prisons to develop and implement a strategy to interdict fentanyl and other synthetic drugs in the mail at Federal correctional facilities.\n#### 1. Short title\nThis Act may be cited as the Bureau Of Prisons Security Check and Action against Narcotics in Mail Act or the BOP SCAN Mail Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Bureau of Prisons has 122 institutions located throughout the United States, employs nearly 38,000 employees, and is responsible for more than 150,000 Federal inmates.\n**(2)**\nInmate mail is a primary entry point for smuggling drugs into correctional facilities, with tainted mail incidents also on the rise.\n**(3)**\nElimination of dangerous contraband, including synthetic drugs, in mail is essential to protecting the health and safety of employees of the Bureau of Prisons and Federal inmates.\n**(4)**\nPrisons in the United States are increasingly deadly facilities, with a 600 percent rise in drug overdoses in recent years.\n**(5)**\nThe introduction of synthetic drugs, particularly fentanyl and fentanyl analogues, into correctional facilities by mail threatens employees, inmates, and the security of correctional institutions, and the practice of deliberately lacing opioids to ensure targeted lethality represents a dramatic emerging concern.\n**(6)**\nThe foregoing factors add tremendous pressures and workload that further burden existing employees, commonly reassigning officers from other functions to assist in processing mail.\n**(7)**\nEmployees at correctional facilities at Federal, State, and local levels continue to request drug interdiction technologies to protect themselves and inmates.\n**(8)**\nA congressionally authorized digital mail scanning pilot program at the Federal Correctional Institution, Beckley, West Virginia, and the United States Penitentiary, Canaan, Pennsylvania, from March 2020 through June 2021, demonstrated effective interdiction technology and practices aimed at eliminating dangerous contraband arriving through the mail and served as an effective deterrent to smuggling attempts.\n**(9)**\nApart from digital mail scanning, there is no widely deployed interdiction technology that has demonstrated a 100 percent efficacy to detecting fentanyl, and other synthetic drugs, arriving through the mail at Bureau of Prisons facilities.\n**(10)**\nRemoving mail processing from Federal prisons and relieving Bureau of Prisons employees from mail sorting duties will result in an extensive budgetary relief to the Bureau of Prisons and decrease the staffing shortages facing prisons.\n#### 3. Definitions\nIn this Act:\n**(1) Director**\nThe term Director means the Director of the Bureau of Prisons.\n**(2) Opioid**\nThe term opioid has the meaning given such term in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 ).\n**(3) Synthetic drug**\nThe term synthetic drug means a controlled substance analogue (as such term is defined in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 )), and includes any analogue of fentanyl.\n#### 4. Strategy to interdict synthetic drugs in postal mail\n##### (a) Evaluation\nNot later than 180 days after the date of enactment of this Act, the Director shall evaluate\u2014\n**(1)**\nthe acquisition and deployment of synthetic drug interdiction equipment and technology by Federal correctional facilities;\n**(2)**\nthe use of technology services by Federal correctional facilities to scan mail; and\n**(3)**\nwhether any technologies used by other Federal agencies or State and local corrections facilities to intercept and interdict contraband in the mail may be used by the Bureau of Prisons.\n##### (b) Strategy\nNot later than 90 days after completing the evaluation under subsection (a), the Director shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a strategy to provide all Federal correctional facilities with capabilities necessary to\u2014\n**(1)**\nprotect staff and inmates from exposure to synthetic drugs and opioids introduced to facilities through the mail;\n**(2)**\nensure that\u2014\n**(A)**\nnot later than 24 hours after a piece of mail is received at a Federal corrections facility or an appropriately contracted offsite location, each inmate receives a digital copy of any mail that is addressed to the inmate;\n**(B)**\nnot later than 30 days after receiving a digital copy of a piece of mail under subparagraph (A), the inmate receives the original physical copy of any mail that\u2014\n**(i)**\ndoes not contain synthetic drugs or opioids; and\n**(ii)**\nis addressed to the inmate; and\n**(C)**\ndelivery to the inmate under subparagraphs (A) and (B) is documented;\n**(3)**\nensure that a process is in place for the processing of legal mail that includes\u2014\n**(A)**\nthe verification of the sender; and\n**(B)**\nmaintains attorney client privilege as required by existing law; and\n**(4)**\nachieve 100 percent scanning capacity of mail arriving at all Federal correction facilities.\n##### (c) Contents\nThe strategy required under subsection (b) shall\u2014\n**(1)**\nidentify critical information technology, digital mail scanning equipment, and mail scanning services necessary to achieve the scanning capacity described in subsection (b)(4);\n**(2)**\ninclude an assessment of operational and logistical considerations, including\u2014\n**(A)**\nprioritization of high security and large inmate population facilities for digital mail scanning infrastructure and security technology deployment;\n**(B)**\nany need for additional personnel and technology training necessary to implement the strategy; and\n**(C)**\nscanning equipment maintenance requirements and periodic digital technology upgrades;\n**(3)**\ninclude an equipment and technology budgetary proposal, for fiscal years 2025 though 2027, in order to fully implement the strategy described under subsection (b); and\n**(4)**\ninclude strategies for conducting oversight of the contractor providing the scanning service for the mail.\n##### (d) Implementation deadline\nNot later than 3 years after the date on which the strategy is submitted under subsection (b), and subject to appropriations, the Director of the Bureau of Prisons shall complete implementation of the submitted plan.\n##### (e) Annual progress reports\nBeginning 1 year after the date on which the strategy is submitted under subsection (b), and each year thereafter, the Director of the Bureau of Prisons shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on the efficiency of the strategy and the total quantity of detected synthetic drugs and opioids.",
      "versionDate": "2025-04-03",
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
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1046",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Marc Fischer Memorial Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-01T15:51:07Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1295is.xml"
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
      "title": "BOP SCAN Mail Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-09T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BOP SCAN Mail Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Bureau Of Prisons Security Check and Action against Narcotics in Mail Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of the Bureau of Prisons to develop and implement a strategy to interdict fentanyl and other synthetic drugs in the mail at Federal correctional facilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:26Z"
    }
  ]
}
```
