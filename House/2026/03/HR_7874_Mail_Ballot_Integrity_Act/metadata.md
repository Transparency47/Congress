# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7874?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7874
- Title: Mail Ballot Integrity Act
- Congress: 119
- Bill type: HR
- Bill number: 7874
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-22T08:07:29Z
- Update date including text: 2026-04-22T08:07:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7874",
    "number": "7874",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Mail Ballot Integrity Act",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:29Z",
    "updateDateIncludingText": "2026-04-22T08:07:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "IN"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "AZ"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "SC"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "FL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "SC"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "FL"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "TN"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "AZ"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "TX"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7874ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7874\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Higgins of Louisiana (for himself, Mr. Stutzman , Mr. Gosar , Mr. Timmons , Mr. Fine , Mrs. Biggs of South Carolina , and Mrs. Luna ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo prohibit a State from distributing unsolicited ballots for voting by mail in any election for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mail Ballot Integrity Act .\n#### 2. Prohibition on unsolicited mail-in ballots and limitation on eligible requests\n##### (a) Prohibition on unsolicited mail-In ballots\nNo State or political subdivision of a State may send, distribute, or otherwise provide a ballot to vote by mail in an election for Federal office to any individual who does not request the State or political subdivision of such State to provide the ballot.\n##### (b) Requirements for mail-In voting in Federal elections\nNotwithstanding any other provision of law, a State shall not issue or transmit a ballot for voting by mail to any individual in the State in an election for Federal office held in the State unless each of the following conditions are met:\n**(1) Request required**\nThe individual submits (in person, by mail, or electronically) a written or electronic request for the ballot that includes an affirmation, under penalty of perjury, that the individual meets one or more of the eligibility criteria under paragraph (2) .\n**(2) Eligibility criteria**\nAn individual who is on the official list of eligible voters in an election for Federal office in a State is eligible to request and receive a mail-in ballot for a Federal election in the State only if the individual\u2014\n**(A)**\nis a member of the uniformed services (as defined in section 101(a) of title 10, United States Code) on active duty, or the spouse or dependent of such a member;\n**(B)**\nis a student, instructor, or professor at an institution of higher education located outside the county in which the voter is registered to vote and resides outside that county by reason thereof, or is the spouse or dependent accompanying and residing with such individual;\n**(C)**\nis a minister, priest, rabbi, or other member of the clergy assigned to a religious post outside the county of registration, or is the spouse or dependent accompanying and residing with such individual;\n**(D)**\nexpects to be temporarily absent from the county in which the voter is registered to vote during the early voting period and on election day;\n**(E)**\nafter the close of voter registration, has moved residence to another county more than 100 miles from the county seat of the former residence;\n**(F)**\nis involuntarily confined in an institution for mental treatment outside the county of registration and is not interdicted or judicially declared incompetent;\n**(G)**\nresides outside the United States;\n**(H)**\nexpects to be hospitalized on election day and did not have knowledge of the hospitalization until after the time for early voting expired (or was hospitalized during early voting, or is restricted to bed by a physician during early voting and on election day);\n**(I)**\nmeets the criteria for participation in a former State program for voters with disabilities in any State that has such a program;\n**(J)**\nis incarcerated in an institution inside or outside the county of registration but is not serving a sentence for a felony conviction;\n**(K)**\nis a participant in a State address confidentiality program;\n**(L)**\nhas a disability and submits documentation with respect to\u2014\n**(i)**\na current mobility impairment identification card with photograph and international symbol of accessibility;\n**(ii)**\ncurrent documentation of eligibility for Social Security disability benefits, veterans disability benefits, paratransit services, benefits from a State office for citizens with developmental disabilities, or benefits from State rehabilitation services; or\n**(iii)**\ncurrent proof of disability from a physician, optometrist, physician assistant, or nurse practitioner; or\n**(M)**\nhas attained the age of 65 years or older.\n##### (c) No permanent or automatic mail-In lists for unqualified voters\nA State may maintain a list of voters who have previously qualified for and requested mail-in ballots in an election for Federal office in the State, but only with respect to voters who continue to meet one or more of the criteria described under subsection (b)(2) as determined under State law.\n##### (d) Effective date\nThis section shall apply with respect to elections for Federal office occurring on and after the date of the enactment of this Act.",
      "versionDate": "2026-03-09",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-03-27T22:00:30Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7874ih.xml"
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
      "title": "Mail Ballot Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mail Ballot Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit a State from distributing unsolicited ballots for voting by mail in any election for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:30Z"
    }
  ]
}
```
