# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2502?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2502
- Title: Law Enforcement Training for Mental Health Crisis Response Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2502
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2025-06-06T08:06:13Z
- Update date including text: 2025-06-06T08:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-03-31 - IntroReferral: Sponsor introductory remarks on measure. (CR H1359)
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-03-31 - IntroReferral: Sponsor introductory remarks on measure. (CR H1359)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2502",
    "number": "2502",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000009",
        "district": "9",
        "firstName": "Marcy",
        "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
        "lastName": "Kaptur",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Law Enforcement Training for Mental Health Crisis Response Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-06T08:06:13Z",
    "updateDateIncludingText": "2025-06-06T08:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1359)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:06:20Z",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "LA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NV"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "IL"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "OK"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "OH"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "GA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NM"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2502ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2502\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Ms. Kaptur (for herself, Mr. Carter of Louisiana , Ms. Titus , Mr. Evans of Pennsylvania , Mr. Casten , and Ms. Brownley ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to authorize a grant program for law enforcement agencies and corrections agencies to obtain behavioral health crisis response training for law enforcement officers and corrections officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Law Enforcement Training for Mental Health Crisis Response Act of 2025 .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nLaw enforcement and corrections officers routinely respond to emergencies involving individuals suffering from a mental health crisis.\n**(2)**\nRecent statistics have shown that as many as\u2014\n**(A)**\n1 in every 10 calls for police response involve a person suffering from a mental illness;\n**(B)**\n1 in every 4 people killed by police suffer from a mental health problem; and\n**(C)**\n1 in 3 people transported to a hospital emergency room for psychiatric reasons are taken by the police.\n**(3)**\nLaw enforcement response calls to individuals suffering from substance use disorder have increased during the current opioid epidemic.\n**(4)**\nThere is a need to ensure that law enforcement officers have access to proper evidence-based training in responding to mental health crises.\n**(5)**\nProper training for response to individuals suffering from a mental health crisis can better protect the safety of the general public and law enforcement officers.\n**(6)**\nLaw enforcement and corrections officers in the United States can better serve their communities if the officers receive training to effectively and safely resolve the mental health crises.\n##### (b) Purpose\nThe purpose of this Act is to provide grants to State, local, and Tribal law enforcement agencies and corrections agencies to obtain behavioral health crisis response training for law enforcement officers and corrections officers to\u2014\n**(1)**\nbetter train law enforcement officers and corrections officers to resolve behavioral health crisis situations;\n**(2)**\nreduce the number of law enforcement officers and corrections officers killed or injured while responding to a behavioral health crisis; and\n**(3)**\nreduce the number of individuals killed or injured during a behavioral health crisis in which a law enforcement officer or corrections officer responds.\n#### 3. Law Enforcement Training for Mental Health Crisis grant program\n##### (a) Reservation of funds\nSection 506 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10157 ) is amended by adding at the end the following:\n(c) Of the total amount made available to carry out this subpart for a fiscal year, the Attorney General may reserve not more than $10,000,000 to carry out the program under section 509. .\n##### (b) Law Enforcement Training for Mental Health Crisis grant program\nSubpart 1 of part E of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10151 et seq. ) is amended by adding at the end the following:\n510. Law Enforcement Training for Mental Health Crisis grant program (a) Grants authorized Subject to the availability of appropriations, the Attorney General is authorized to award grants to applicants for\u2014 (1) law enforcement officers or corrections officers to receive training from a program; and (2) the cost of transportation and lodging associated with law enforcement officers or corrections officers attending such program. (b) Program standards The Attorney General shall establish and publish qualification standards for organizations that provide programs. (c) Applications The head of an applicant shall submit to the Attorney General an application that\u2014 (1) shall include\u2014 (A) a statement describing the program the law enforcement officers or corrections officers will complete; (B) the total number of law enforcement officers or corrections officers in the agency; (C) the number of law enforcement officers or corrections officers of the agency that have been killed, or seriously injured while responding to a behavioral health crisis during the 5-year period preceding the date of the application; and (D) whether the law enforcement officers or corrections officers employed by the agency receive any behavioral health crisis response training, including during basic officer training; and (2) in addition to the information required under paragraph (1), may, at the option of the applicant, include information relating to\u2014 (A) recent incidents involving officers of the agency during which behavioral health crisis response training could have played a role in protecting the safety of\u2014 (i) the law enforcement officer or the public, including the person or persons the law enforcement officers encountered; or (ii) the corrections officer or inmates at the correctional facility; and (B) estimated cost of attendance of a program per officer. (d) Restrictions (1) Supplemental funds Grant funds shall be used to supplement, and not supplant, State, local, and Tribal funds made available to any applicant for any of the purposes described in subsection (a). (2) Administrative costs Not more than 3 percent of any grant made under this section may be used for administrative costs. (e) Reports and records (1) Reports For each year during which grant funds are used, the recipient shall submit to the Attorney General a report containing\u2014 (A) a summary of any activity carried out using grant funds; (B) the number of officers that received training using grant funds; and (C) any other information relevant to the purpose of this Act that the Attorney General may determine appropriate. (2) Records For the purpose of an audit by the Attorney General of the receipt and use of grant funds, a recipient shall\u2014 (A) keep\u2014 (i) any record relating to the receipt and use of grant funds; and (ii) any other record as the Attorney General may require; and (B) make the records described in subparagraph (A) available to the Attorney General upon request by the Attorney General. (f) Definitions In this section: (1) Applicant The term applicant means a law enforcement agency or corrections agency that applies for a grant under this section. (2) Attorney general The term Attorney General means the Attorney General, acting through the Assistant Attorney General for the Office of Justice Programs. (3) Grant funds The term grant funds means funds from a grant awarded under this section. (4) Law enforcement agency The term law enforcement agency means an agency of a State or unit of local government that is authorized by law or by a government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of criminal law. (5) Program The term program means a program or class that\u2014 (A) provides instructional training to law enforcement officers or corrections officers for response to a behavioral health crisis, including response to people suspected to be under the influence of a drug or psychoactive substance, and response to circumstances in which a person is suspected to be suicidal or experiencing a mental illness; (B) includes training on techniques and strategies designed to protect\u2014 (i) the health and safety of law enforcement officers and the public, including the person or persons a law enforcement officer encounters during a behavioral health crisis response; or (ii) the health and safety of corrections officers and inmates at the correctional facility, including the inmate a corrections officer encounters during a behavioral health crisis response, or in the normal course of business of interactions with the inmate; and (C) is developed in conjunction with healthcare professionals and people with lived experiences of mental health illness to provide crisis intervention training focused on understanding mental and behavioral health, developing empathy, navigating community resources, de-escalation and communications skills, and practical application training for officers. (6) Recipient The term recipient means an applicant that receives a grant under this section. .",
      "versionDate": "2025-03-31",
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
        "updateDate": "2025-04-07T14:16:24Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2502ih.xml"
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
      "title": "Law Enforcement Training for Mental Health Crisis Response Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Law Enforcement Training for Mental Health Crisis Response Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to authorize a grant program for law enforcement agencies and corrections agencies to obtain behavioral health crisis response training for law enforcement officers and corrections officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:44Z"
    }
  ]
}
```
