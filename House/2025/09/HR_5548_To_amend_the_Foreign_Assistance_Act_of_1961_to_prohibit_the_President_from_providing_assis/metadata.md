# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5548?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5548
- Title: Fraud Accountability and Recovery Act
- Congress: 119
- Bill type: HR
- Bill number: 5548
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2026-03-25T08:06:09Z
- Update date including text: 2026-03-25T08:06:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-09-23: Introduced in House

## Actions

- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5548",
    "number": "5548",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Fraud Accountability and Recovery Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:06:09Z",
    "updateDateIncludingText": "2026-03-25T08:06:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "MN"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "OH"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "MN"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "TN"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "FL"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "CO"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "SC"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "MI"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5548ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5548\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Mr. Finstad introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Foreign Assistance Act of 1961 to prohibit the President from providing assistance to the government of any country that has failed to extradite an individual that has been convicted of committing fraud against the United States or that has failed to take all appropriate measures with respect to assisting the recoupment of those funds.\n#### 1. Short title\nThis Act may be cited as the Fraud Accountability and Recovery Act .\n#### 2. Prohibition on assistance\nSection 620 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2370 ) is amended by adding at the end the following new subsection:\n(z) No assistance shall be furnished under this Act to the government of any country the President determines\u2014 (1) has failed to extradite an individual convicted of committing fraud against the United States or benefitting from the proceeds of defrauding the United States; or (2) has failed to take all appropriate legal, administrative, or enforcement measures to assist in the recoupment of Federal funds fraudulently stolen from the United States by identifying, freezing, seizing, and repatriating the funds so fraudulently obtained. .\n#### 3. Findings\nCongress finds the following:\n**(1)**\nAccording to the Government Accountability Office, the Federal Government lost between $233,000,000,000 and $521,000,000,000 annually to fraud from fiscal years 2018 through 2022.\n**(2)**\nThe range reflects the varying risk environments for fraud\u2014ninety percent of the estimated fraud losses fell in this range.\n**(3)**\nIn Minnesota, the nonprofit organization Feeding Our Future and associated individuals carried out the largest COVID\u201319 pandemic fraud scheme in the United States, stealing over $250,000,000 intended to feed hungry children.\n**(4)**\nThe Department of Justice has charged 75 defendants in the fraud scheme, and Federal prosecutors have secured multiple convictions against participants in this scheme, which involved the submission of false reimbursement claims, the creation of fictitious meal sites, and the laundering of Federal funds through shell entities and fraudulent invoices.\n**(5)**\nCharges and convictions in the Feeding Our Future scheme include\u2014\n**(A)**\nwire fraud;\n**(B)**\nconspiracy to commit wire fraud;\n**(C)**\ntheft of government funds;\n**(D)**\nconspiracy to defraud the United States;\n**(E)**\nFederal program bribery;\n**(F)**\nmoney laundering; and\n**(G)**\nengaging in monetary transactions with criminally derived property.\n**(6)**\nSome of the proceeds of this fraud were used to purchase luxury real estate and vehicles, and at least one defendant transferred funds and property abroad, including to Kenya, beyond the reach of United States authorities.\n#### 4. Sense of Congress\nIt is the sense of Congress as follows:\n**(1)**\nThe United States lacks adequate tools to ensure the recovery of stolen taxpayer funds and property transferred overseas, leaving American taxpayers without recourse when foreign jurisdictions fail to cooperate.\n**(2)**\nStrengthening program integrity, recouping stolen funds, and preventing individuals convicted of defrauding Federal programs from seeking international harbor are essential to safeguarding taxpayer dollars and ensuring programs assist those that Congress intended.\n**(3)**\nProviding additional deterrence by ensuring potential fraudsters lack a safe harbor abroad is critical to preventing future fraud schemes.\n#### 5. Waiver\n##### (a) In general\nThe President may waive the limitation under section 620(z) of the Foreign Assistance Act of 1961, as added by section 2, if the President certifies to Congress that prohibiting such assistance is contrary to the national security of the United States.\n##### (b) Prior notification\nNot later than 15 days before the entry into effect of a waiver under subsection (a), the President shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a notification of intent to issue such a waiver, along with a justification.\n#### 6. Report on noncompliant countries\nNot later than 180 days after the date of enactment of this Act, and annually thereafter, the Secretary of State shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a report that\u2014\n**(1)**\nlists each country the President determines has failed to take all appropriate legal, administrative, or enforcement measures as described in section 620(z)(2) of the Foreign Assistance Act of 1961 (as added by section 2); and\n**(2)**\ndescribes the total amount of fraudulently obtained funds and court-ordered remedies, such as recoveries, restitution, or fines, along with seizures and forfeitures from the United States attributable to the failure to take all such measures by each such country.",
      "versionDate": "2025-09-23",
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
        "name": "International Affairs",
        "updateDate": "2025-12-16T19:03:22Z"
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
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5548ih.xml"
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
      "title": "Fraud Accountability and Recovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fraud Accountability and Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Foreign Assistance Act of 1961 to prohibit the President from providing assistance to the government of any country that has failed to extradite an individual that has been convicted of committing fraud against the United States or that has failed to take all appropriate measures with respect to assisting the recoupment of those funds.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T06:18:27Z"
    }
  ]
}
```
