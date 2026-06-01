# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4317?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4317
- Title: No Licenses for Illegal Drivers or Truckers Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4317
- Origin chamber: Senate
- Introduced date: 2026-04-16
- Update date: 2026-05-13T17:26:09Z
- Update date including text: 2026-05-13T17:26:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in Senate
- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works. (Sponsor introductory remarks on measure: CR S1822-1823; text: CR S1823-1824)
- Latest action: 2026-04-16: Introduced in Senate

## Actions

- 2026-04-16 - IntroReferral: Introduced in Senate
- 2026-04-16 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works. (Sponsor introductory remarks on measure: CR S1822-1823; text: CR S1823-1824)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4317",
    "number": "4317",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "No Licenses for Illegal Drivers or Truckers Act of 2026",
    "type": "S",
    "updateDate": "2026-05-13T17:26:09Z",
    "updateDateIncludingText": "2026-05-13T17:26:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works. (Sponsor introductory remarks on measure: CR S1822-1823; text: CR S1823-1824)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T16:39:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "WY"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4317is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4317\nIN THE SENATE OF THE UNITED STATES\nApril 16 (legislative day, April 14), 2026 Mr. Barrasso (for himself, Mr. Cornyn , Ms. Lummis , and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend title 23, United States Code, to withhold Federal highway funding from States that issue driver\u2019s licenses, commercial driver\u2019s licenses, or personal identification cards to individuals without verifying the legal status of those individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Licenses for Illegal Drivers or Truckers Act of 2026 .\n#### 2. Preserving the integrity of State-issued driver\u2019s licenses, commercial driver\u2019s licenses, and personal identification cards\n##### (a) In general\nChapter 1 of title 23, United States Code, is amended by inserting after section 154 the following:\n155. Preserving the integrity of State-issued driver's licenses, commercial driver's licenses, and personal identification cards (a) Definitions In this section: (1) Commercial driver\u2019s license The term commercial driver\u2019s license has the meaning given the term in section 31301 of title 49. (2) Driver\u2019s license The term driver\u2019s license means a motor vehicle operator\u2019s license (as defined in section 30301 of title 49). (3) Evidence of lawful presence The term evidence of lawful presence means valid, unexpired documentary evidence issued by the Secretary of Homeland Security that a person is\u2014 (A) a citizen or national of the United States; or (B) an alien lawfully admitted for permanent residence (as those terms are defined in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) )). (4) Personal identification card The term personal identification card means an identification document (as defined in section 1028(d) of title 18) issued by a State. (b) Withholding of funds for noncompliance (1) In general On October 1, 2026, and each October 1 thereafter, the Secretary shall withhold from a State 10 percent of the amounts required to be apportioned to the State under paragraphs (1) through (8) of section 104(b) for a fiscal year if that State does not have in effect and is enforcing a law that meets the requirements described in subsection (e). (2) Duration If, before the last day of the fiscal year for which funds are withheld under this section, the Secretary determines that the State is in compliance with this section, the Secretary shall, on the first day on which the Secretary makes that determination, apportion to the State the funds withheld from that State for that fiscal year under this section. (c) Redistribution of withheld funds On the first October 1 after a fiscal year for which amounts were withheld from a State under this section, the Secretary shall redistribute those amounts to States that are in compliance with this section so that each State in compliance with this section receives an amount equal to the proportion that\u2014 (1) the amount apportioned to the State under section 104(b); bears to (2) the total amount apportioned to all States in compliance with this section under section 104(b). (d) Effect of withholding Except as provided in subsection (b), no funds withheld under this section from apportionment to a State shall be available to a State. (e) Law To require and verify lawful presence (1) In general A State shall be in compliance with this section if the State has in effect and is enforcing a law to require and subsequently verify evidence of lawful presence from each applicant for a driver\u2019s license, commercial driver\u2019s license, or personal identification card issued by the State. (2) Requirement A law referred to in paragraph (1) shall employ a means approved by the Secretary of Homeland Security\u2014 (A) to confirm the identity of an applicant for a driver\u2019s license, commercial driver\u2019s license, or personal identification card through electronic validation of biographic and biometric information, including the name, photograph, and fingerprints of the applicant; (B) to confirm the validity of the lawful presence of an applicant described in subparagraph (A), including whether the applicant has lawfully maintained that lawful presence, through the results of background and security checks, including fingerprint checks by the Federal Bureau of Investigation; and (C) to verify the authenticity of the evidence of lawful presence provided by an applicant described in subparagraph (A), which shall include an identity document containing a photograph, by confirming the social security number or individual taxpayer identification number of the applicant with, as applicable\u2014 (i) the Internal Revenue Service; (ii) the Social Security Administration; or (iii) the Systematic Alien Verification for Entitlements program of U.S. Citizenship and Immigration Services. (f) REAL ID Act of 2005 Nothing in this section affects any State requirement under title II of the REAL ID Act of 2005 ( 49 U.S.C. 30301 note; Public Law 109\u201313 ). .\n##### (b) Clerical amendment\nThe analysis for chapter 1 of title 23, United States Code, is amended by inserting after the item relating to section 154 the following:\n155. Preserving the integrity of State-issued driver's licenses, commercial driver's licenses, and personal identification cards. .",
      "versionDate": "2026-04-16",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2026-05-13T17:26:08Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4317is.xml"
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
      "title": "No Licenses for Illegal Drivers or Truckers Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T04:53:37Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Licenses for Illegal Drivers or Truckers Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 23, United States Code, to withhold Federal highway funding from States that issue driver's licenses, commercial driver's licenses, or personal identification cards to individuals without verifying the legal status of those individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T04:48:59Z"
    }
  ]
}
```
