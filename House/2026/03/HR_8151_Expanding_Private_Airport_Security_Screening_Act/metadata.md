# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8151?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8151
- Title: Expanding Private Airport Security Screening Act
- Congress: 119
- Bill type: HR
- Bill number: 8151
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-05-16T08:07:26Z
- Update date including text: 2026-05-16T08:07:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-30 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2026-03-27: Introduced in House

## Actions

- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-30 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8151",
    "number": "8151",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Expanding Private Airport Security Screening Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:26Z",
    "updateDateIncludingText": "2026-05-16T08:07:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-30",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-27",
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
          "date": "2026-03-28T01:33:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-30T19:47:28Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "MO"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "GA"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8151ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8151\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Mr. Perry (for himself, Mr. Burlison , Mr. Roy , and Mr. Clyde ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend title 49, United States Code, to allow airport operators to enter into contracts with qualified private screening companies to carry out the screening of passengers and property at airports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding Private Airport Security Screening Act .\n#### 2. Qualified private screening company services\nSection 44920 of title 49, United States Code, is amended to read as follows:\n44920. Screening partnership program (a) Screening partnership program contracts (1) In general An airport operator may enter into a contract with a qualified private screening company on the list maintained under subsection (b) to carry out the screening of passengers and property at the airport under section 44901. (2) Notification Not less than 7 days after entering into a contract with a qualified private screening company under paragraph (1), an airport operator shall notify the Administrator of the Transportation Security Administration. (b) Public list of qualified private screening companies (1) In general The Administrator shall maintain a publicly available list of qualified private screening companies that meet the requirements of paragraph (3). (2) Application To be included in the list maintained under paragraph (1), a qualified private screening company shall submit an application to the Administrator in such form, in such manner, and containing such information as the Administrator may require. (3) Requirements A qualified private screening company is eligible to be included in the list maintained under paragraph (1) if the company\u2014 (A) only employs individuals to provide such services who meet all the requirements of this chapter applicable to Federal Government personnel who perform passenger and property security screening services at airports under this chapter; (B) demonstrates capability of providing passenger and property screening services and protection at the same level provided by Federal Government personnel under this chapter; and (C) is owned and controlled by a citizen of the United States, to the extent that the Administrator determines that there are private screening companies owned and controlled by such citizens. (c) Transition plan Not later than 30 days after the date on which an airport operator provides the notification required under subsection (a)(2), the airport operator shall create a plan to transition the provision of passenger and property screening services at such airport to the applicable qualified private screening company. (d) Supervision of screening personnel The Administrator shall\u2014 (1) provide Federal Government supervisors to oversee all screening at each airport at which passenger and property screening services are provided under this section and provide Federal Government law enforcement officers at the airport pursuant to this chapter; and (2) undertake covert testing and remedial training support for employees of qualified private screening companies providing passenger and property screening services at airports. (e) Operator of airport (1) In general Notwithstanding any other provision of law, an operator of an airport shall not be liable for any claims for damages filed in State or Federal court (including a claim for compensatory, punitive, contributory, or indemnity damages) related to an act of negligence, gross negligence, or intentional wrongdoing by\u2014 (A) a qualified private screening company or any of its employees in any case in which the qualified private screening company is acting under a contract entered into with the airport operator; or (B) employees of the Federal Government providing supervision of screening personnel at the airport. (2) Rule of construction Nothing in this subsection shall relieve any airport operator from liability for its own acts or omissions related to its security responsibilities, nor except as may be provided by the Support Anti-Terrorism by Fostering Effective Technologies Act of 2002 shall it relieve any qualified private screening company or its employees from any liability related to its own acts of negligence, gross negligence, or intentional wrongdoing. (f) Report to Congress (1) In general The Administrator shall submit an annual report to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Homeland Security of the House of Representatives that contains\u2014 (A) a comparison of the mean average screening performance of qualified private screening companies under contract pursuant to this section and the mean average screening performance of all airports using Federal Government passenger and property screening services; (B) a comparison of the mean cost of providing passenger and property screening services with Federal Government personnel and the mean cost of contracting with a qualified private screening company for such services under this section delineated by airport category; and (C) a comparison of the cost to each airport operator of contracting with a qualified private screening company to provide passenger and property screening services under this section to the estimated cost to the Federal Government to provide passenger and property security screening services at such airport. (2) Cost estimates Any estimate of cost to the Federal Government provided pursuant to paragraph (1) shall reflect the total cost to the Federal Government, including all costs incurred by all Federal agencies of providing passenger and property screening services at an airport. (3) Publication Not later than 7 days after the date on which the Administrator submits a report required under paragraph (1), the Administrator shall publish such report on a website of the Transportation Security Administration. .\n#### 3. Providing effective cost comparisons to airport operators\nSection 1947 of the FAA Reauthorization Act of 2018 ( 49 U.S.C. 44901 note) is amended\u2014\n**(1)**\nin paragraph (1) by striking and at the end;\n**(2)**\nin paragraph (2)(B)(iii) by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(3) in the case of an airport operator that contracts with a qualified private screening company to provide passenger and property screening services at such airport, a comparison of the cost of such contract and an estimate of the cost to such airport operator of providing passenger and property screening services with Federal Government personnel. .",
      "versionDate": "2026-03-27",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-14T13:43:33Z"
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
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8151ih.xml"
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
      "title": "Expanding Private Airport Security Screening Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Private Airport Security Screening Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to allow airport operators to enter into contracts with qualified private screening companies to carry out the screening of passengers and property at airports, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:45Z"
    }
  ]
}
```
