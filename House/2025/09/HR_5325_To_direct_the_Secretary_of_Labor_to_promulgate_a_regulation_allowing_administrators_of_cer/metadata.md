# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5325?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5325
- Title: Unclaimed Retirement Rescue Plan
- Congress: 119
- Bill type: HR
- Bill number: 5325
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2026-03-26T08:06:43Z
- Update date including text: 2026-03-26T08:06:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5325",
    "number": "5325",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001223",
        "district": "2",
        "firstName": "Seth",
        "fullName": "Rep. Magaziner, Seth [D-RI-2]",
        "lastName": "Magaziner",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Unclaimed Retirement Rescue Plan",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:43Z",
    "updateDateIncludingText": "2026-03-26T08:06:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-11T13:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "KS"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "KS"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "IL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "IL"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "KS"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "WY"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "WA"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "AL"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "MD"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "NE"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "VT"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "PA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "VA"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "CA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5325ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5325\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Magaziner (for himself and Mr. Estes ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Labor to promulgate a regulation allowing administrators of certain pension plans to voluntarily transfer unclaimed retirement distributions to State unclaimed property programs.\n#### 1. Short title\nThis Act may be cited as the Unclaimed Retirement Rescue Plan .\n#### 2. Unclaimed retirement distributions regulation\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of Labor shall promulgate a regulation described in subsection (b).\n##### (b) Regulation described\nThe regulation described in this subsection shall\u2014\n**(1)**\ncomply with the requirements of this section; and\n**(2)**\nallow administrators of pension plans and other responsible fiduciaries to transfer unclaimed retirement distributions to State unclaimed property programs through the States\u2019 Unclaimed Retirement Clearing House that manages the voluntary transfer of funds nationally across State unclaimed property programs.\n##### (c) Prerequisites for plan and other responsible fiduciary transfers to States\n**(1) In general**\nPrior to transferring unclaimed retirement distributions to State unclaimed property programs, a plan or other responsible fiduciary shall, with respect to unclaimed retirement distributions that are $50 or more\u2014\n**(A)**\nto the extent that it has not already done so, attempt to identify, through an informational database search and through a search of a commercially reasonable outside source, the current address and other contact information, such as a phone number or email address of a participant or other beneficiary owed such a distribution if the plan or other responsible fiduciary has reason to believe that contact information of such participant or beneficiary available to the plan or the fiduciary is inaccurate; and\n**(B)**\nsend a notice to the participant or beneficiary entitled to such a distribution that\u2014\n**(i)**\nexplains that the plan or other responsible fiduciary is in possession of the distribution and that absent a timely response from the participant or beneficiary, the distribution will be transferred to the State unclaimed property program of the State where the participant or other party last resided; and\n**(ii)**\nprovides instructions to the participant or beneficiary to prevent the transfer of the distribution to a State unclaimed property program.\n**(2) Form of notice**\nFor the purposes of sending a notice described in paragraph (1)(B), the plan administrator or other responsible fiduciary may determine the form of sending such notice, so long as such notice\u2014\n**(A)**\nis reasonably expected to reach the participant or beneficiary; and\n**(B)**\nis sent in a secure means, such as through email, an online portal, or the mail, and protects the personal information of participants and beneficiaries.\n**(3) Mailing not required**\nThe sending of a notice described in paragraph (1) shall not be required if, following completion of the search required by paragraph (1)(A), the search does not provide updated contact information for a participant or beneficiary.\n##### (d) Plan or fiduciary relief\nNotwithstanding any other provision of law, the administrator of a pension plan or other fiduciary that satisfies the requirements of this section and any applicable regulations when making a transfer to a State unclaimed property program shall, with respect to such transfer, be deemed to have satisfied the requirements of sections 404(a) and 406 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1104(a) ; 1106).\n##### (e) Information sharing mechanism\nFor the purposes of updating plan records and ensuring compliance with section 404 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1104 ), the Secretary shall make available to plan administrators a means of verifying whether a distribution transferred under this section to a State unclaimed property program has been claimed by a participant or beneficiary.\n##### (f) Report required\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, and every 90 days thereafter, a plan fiduciary shall submit to the Secretary of Labor a report that includes\u2014\n**(A)**\nwith respect to each transfer of an unclaimed retirement distribution to a State unclaimed property program that has not been reported to the Secretary\u2014\n**(i)**\nthe name, social security number, date of birth, and last known address of the participant or beneficiary entitled to the unclaimed retirement distribution, including any applicable qualified domestic relations order (as defined in section 206 (d)(3)(B)(i) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1056(d)(3)(B)(i) ));\n**(ii)**\nthe amount of the distribution transferred;\n**(iii)**\nthe State to which the transfer was made; and\n**(iv)**\nthe name of the plan or responsible fiduciary who transferred the distribution; and\n**(B)**\nwith respect to any transfer of an unclaimed retirement distribution to a State unclaimed property program that has been claimed by a participant or beneficiary, an identification of such transfer.\n**(2) Report not subject to public disclosure**\nA report required under this subsection shall not be subject to public disclosure under section 552 of title 5, United States Code.\n**(3) Retirement Savings Lost and Found**\n**(A) In general**\nThe Secretary of Labor shall include all information submitted under paragraph (1) and any information received pursuant to the mechanism established under subsection (d) in the Retirement Savings Lost and Found Database, established pursuant to section 523 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1153 ).\n**(B) Collected distributions**\nFrom the information received under this subsection, indicate in such database the distributions that were claimed by a participant or beneficiary.\n##### (g) Participant data\nA pension plan or fiduciary will not violate section 404(a) of the Employee Retirement Income Security Act and shall not be subject to liability for transmitting participant data to a State unclaimed property program through a national clearinghouse, provided that the pension plan or fiduciary exercises reasonable care in making the transmittal.\n##### (h) Treatment of transfer for purposes of qualified trust rules\nA trust forming part of a pension plan shall not be treated as failing to constitute a qualified trust under section 401 of the Internal Revenue Code of 1986 merely because the pension plan of which such trust is a part makes a transfer that meets the requirements of this section and the regulations promulgated thereunder.\n##### (i) Congressional report\nNot later than 24 months after the promulgation of the regulation described in subsection (a), the Secretary of Labor shall submit to Congress a report\u2014\n**(1)**\non the progress and effectiveness of the regulation; and\n**(2)**\nany recommendations on how to improve the regulation.\n##### (j) Definitions\nIn this Act:\n**(1) Contact information**\nThe term contact information , with respect to a participant or beneficiary, means identifying information, including a mailing address, phone number, or email address.\n**(2) ERISA terms**\nIn this Act, the terms administrator , fiduciary , and pension plan have the meanings given the terms in section 3 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1003 ).\n**(3) Informational database**\nThe term informational database means a commercially available database or a government-provided database.\n**(4) Outside source**\nThe term outside source means a commercial locator database, address verification service, or a publicly or commercially accessible database.\n**(5) State unclaimed property program**\nAs used in this Act, the term State unclaimed property program means the statutory-based initiative undertaken by the 50 State, the District of Columbia, Puerto Rico, and the United States Virgin Islands to safeguard and return financial assets that have become unclaimed or forgotten by their owners.\n**(6) Unclaimed retirement distribution**\n**(A) In general**\nThe term unclaimed retirement distribution means\u2014\n**(i)**\nwith respect to a pension plan that has undergone or is in the process of termination, any distribution that has not been cashed or otherwise claimed within the 90-day period beginning on the date that the distribution became payable; or\n**(ii)**\nwith respect to any other pension plan, any single unpaid obligation owed to a participant or beneficiary by such a pension plan that has not been cashed or otherwise claimed for a 12-month period beginning on the date that the such obligation became payable, and does not exceed $5,000, regardless of\u2014\n**(I)**\nthe basis for the obligation;\n**(II)**\nwhether an attempt to distribute the obligation was returned as undeliverable; or\n**(III)**\nwhether it has been previously reduced to a check or other form of payment.\n**(B) Maximum amount**\nThe Secretary of Labor may, in their discretion, increase the $5,000 limit in clause (ii) of subparagraph (A).",
      "versionDate": "2025-09-11",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-24T15:23:03Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5325ih.xml"
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
      "title": "Unclaimed Retirement Rescue Plan",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-23T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Unclaimed Retirement Rescue Plan",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-23T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Labor to promulgate a regulation allowing administrators of certain pension plans to voluntarily transfer unclaimed retirement distributions to State unclaimed property programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-23T04:18:25Z"
    }
  ]
}
```
