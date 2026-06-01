# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2150?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2150
- Title: Women’s Health Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2150
- Origin chamber: Senate
- Introduced date: 2025-06-24
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in Senate
- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-24: Introduced in Senate

## Actions

- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2150",
    "number": "2150",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Women\u2019s Health Protection Act of 2025",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T20:23:14Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CT"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "WA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MD"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CO"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "WA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "AZ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-24",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NM"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CT"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "GA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-24",
      "state": "VT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NH"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "VA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "GA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2150is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2150\nIN THE SENATE OF THE UNITED STATES\nJune 24, 2025 Ms. Baldwin (for herself, Mr. Blumenthal , Mr. Schumer , Mrs. Murray , Mr. Durbin , Ms. Alsobrooks , Mr. Bennet , Ms. Blunt Rochester , Mr. Booker , Ms. Cantwell , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Fetterman , Mr. Gallego , Mrs. Gillibrand , Ms. Hassan , Mr. Heinrich , Mr. Hickenlooper , Ms. Hirono , Mr. Kaine , Mr. Kelly , Mr. Kim , Mr. King , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Markey , Mr. Merkley , Mr. Murphy , Mr. Ossoff , Mr. Padilla , Mr. Peters , Mr. Reed , Ms. Rosen , Mr. Sanders , Mr. Schatz , Mr. Schiff , Mrs. Shaheen , Ms. Slotkin , Ms. Smith , Mr. Van Hollen , Mr. Warner , Mr. Warnock , Ms. Warren , Mr. Welch , Mr. Whitehouse , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo protect a person\u2019s ability to determine whether to continue or end a pregnancy, and to protect a health care provider\u2019s ability to provide abortion services.\n#### 1. Short title\nThis Act may be cited as the Women\u2019s Health Protection Act of 2025 .\n#### 2. Purpose\nThe purposes of this Act are as follows:\n**(1)**\nTo permit people to seek and obtain abortion services, and to permit health care providers to provide abortion services, without harmful or unwarranted limitations or requirements that single out the provision of abortion services for restrictions that are more burdensome than those restrictions imposed on medically comparable procedures, do not, on the basis of the weight of established clinical practice guidelines consistent with medical evidence, significantly advance reproductive health or the safety of abortion services, or make abortion services more difficult to access.\n**(2)**\nTo promote access to abortion services and thereby protect women\u2019s ability to participate equally in the economic and social life of the United States.\n**(3)**\nTo protect people\u2019s ability to make decisions about their bodies, medical care, family, and life\u2019s course.\n**(4)**\nTo eliminate unwarranted burdens on commerce and the right to travel. Abortion bans and restrictions invariably affect commerce over which the United States has jurisdiction. Health care providers engage in economic and commercial activity when they provide abortion services. Moreover, there is an interstate market for abortion services and, in order to provide such services, health care providers engage in interstate commerce to purchase medicine, medical equipment, and other necessary goods and services; to obtain and provide training; and to employ and obtain commercial services from health care personnel, many of whom themselves engage in interstate commerce, including by traveling across State lines. Individuals engage in the interstate market by purchasing abortion services, including the purchase, use, and consumption of medicine, medical equipment, and other necessary goods and services transited in the stream of interstate commerce, the receipt of telemedicine services, and traveling across State lines to purchase and receive abortion services or assist others in purchasing or receiving such services. The increase in abortion prohibitions and restrictions in a subset of States since 2022 cause women to travel to other States for abortion care, which, in turn, affects the health care systems of those States that provide the treatment and has exponentially increased the burden on interstate commerce and the instrumentalities of interstate commerce. Congress has the authority to enact this Act to protect access to abortion services pursuant to\u2014\n**(A)**\nits powers under the commerce clause of section 8 of Article I of the Constitution of the United States;\n**(B)**\nits powers under section 5 of the Fourteenth Amendment to the Constitution of the United States to enforce the provisions of section 1 of the Fourteenth Amendment; and\n**(C)**\nits powers under the necessary and proper clause of section 8 of Article I of the Constitution of the United States.\n#### 3. Definitions\nIn this Act:\n**(1) Abortion services**\nThe term abortion services means an abortion and any medical or non-medical services related to and provided in conjunction with an abortion (whether or not provided at the same time or on the same day as the abortion).\n**(2) Government**\nThe term government includes each branch, department, agency, instrumentality, and official of the United States or a State.\n**(3) Health care provider**\nThe term health care provider means any entity (including any hospital, clinic, or pharmacy (whether physical, mobile, or virtual)) or individual (including any physician, certified nurse-midwife, nurse practitioner, advanced practice clinician, registered nurse, pharmacist, or physician assistant) that\u2014\n**(A)**\nis engaged or seeks to engage in the delivery of health care services, including abortion services; and\n**(B)**\nif required by law or regulation to be licensed or certified to engage in the delivery of such services\u2014\n**(i)**\nis so licensed or certified; or\n**(ii)**\nwould be so licensed or certified but for their past, present, or potential provision of abortion services protected by section 4.\n**(4) Medically comparable procedures**\nThe term medically comparable procedures means medical procedures that are similar, on the basis of the weight of established clinical practice guidelines consistent with medical evidence, in terms of health and safety risks to the patient, complexity, or the clinical setting that is indicated.\n**(5) Pregnancy**\nThe term pregnancy refers to the period of the human reproductive process beginning with the implantation of a fertilized egg.\n**(6) State**\nThe term State includes the District of Columbia, the Commonwealth of Puerto Rico, and each territory and possession of the United States, and any subdivision of any of the foregoing, including any unit of local government, such as a county, city, town, village, or other general purpose political subdivision of a State.\n**(7) Viability**\nThe term viability means the point in a pregnancy at which, in the good-faith medical judgment of the treating health care provider, and based on the particular facts of the case before the health care provider, there is a reasonable likelihood of sustained fetal survival outside the uterus with or without artificial support.\n#### 4. Protected activities and services\n##### (a) General rules\n**(1) Pre-viability**\nA health care provider has a right under this Act to provide such abortion services, and a patient has a corresponding right under this Act to terminate a pregnancy prior to viability without being subject to any of the following limitations or requirements:\n**(A)**\nA prohibition on abortion prior to viability, including a prohibition or restriction on a particular abortion procedure or method, or a prohibition on providing or obtaining such abortions.\n**(B)**\nA limitation on a health care provider\u2019s ability to prescribe or dispense drugs that could be used for reproductive health purposes based on current evidence-based regimens or the provider\u2019s good-faith medical judgment, or a limitation on a patient\u2019s ability to receive or use such drugs, other than a limitation generally applicable to the prescription, dispensing, or distribution of drugs.\n**(C)**\nA limitation on a health care provider\u2019s ability to provide, or a patient\u2019s ability to receive, abortion services via telemedicine, other than a limitation generally applicable to the provision of medically comparable services via telemedicine.\n**(D)**\nA limitation or prohibition on a patient\u2019s ability to receive, or a provider\u2019s ability to provide, abortion services in a State based on the State of residency of the patient, or a prohibition or limitation on the ability of any individual to assist or support a patient seeking abortion.\n**(E)**\nA requirement that a health care provider perform specific tests or medical procedures in connection with the provision of abortion services (including prior to or subsequent to the abortion), unless such tests or procedures are standard to the weight of established clinical practice guidelines consistent with medical evidence pertaining to abortion services.\n**(F)**\nA requirement that a health care provider offer or provide a patient seeking abortion services medically inaccurate information that is not compatible with the weight of established clinical practice guidelines.\n**(G)**\nA limitation or requirement concerning the physical plant, equipment, staffing, or hospital transfer arrangements of facilities where abortion services are provided, or the credentials or hospital privileges or status of personnel at such facilities, that is not imposed on facilities or the personnel of facilities where medically comparable procedures are performed.\n**(H)**\nA requirement that, prior to obtaining an abortion, a patient make one or more medically unnecessary in-person visits to the provider of abortion services or to any individual or entity that does not provide abortion services.\n**(I)**\nA limitation on a health care provider\u2019s ability to provide immediate abortion services when that health care provider believes, based on the good-faith medical judgment of the provider, that delay would pose a risk to the patient\u2019s life or health.\n**(J)**\nA requirement that a patient seeking abortion services at any point or points in time prior to viability disclose the patient\u2019s reason or reasons for seeking abortion services, or a limitation on providing or obtaining abortion services at any point or points in time prior to viability based on any actual, perceived, or potential reason or reasons of the patient for obtaining abortion services, regardless of whether the limitation is based on a health care provider\u2019s actual or constructive knowledge of such reason or reasons.\n**(2) Post-viability**\n**(A) In general**\nA health care provider has a right under this Act to provide abortion services and a patient has a corresponding right under this Act to terminate a pregnancy after viability when, in the good-faith medical judgement of the treating health care provider, it is necessary to protect the life or health of the patient. This subparagraph shall not otherwise apply after viability.\n**(B) Additional circumstances**\nA State may provide additional circumstances under which post viability abortions are permitted.\n**(C) Limitation**\nIn the case where a termination of a pregnancy after viability, in the good-faith medical judgement of the treating health care provider, is necessary to protect the life or health of the patient, none of the limitations or requirements described in paragraph (1) shall be imposed by law.\n##### (b) Other limitations or requirements\nThe rights described in subsection (a) shall not be limited or otherwise infringed through any other limitation or requirement that\u2014\n**(1)**\nexpressly, effectively, implicitly, or as implemented, targets abortion, the provision of abortion services, individuals who seek abortion services or who provide assistance and support to those seeking abortion services, health care providers who provide abortion services, or facilities in which abortion services are provided; and\n**(2)**\nimpedes access to abortion services.\n##### (c) Factors for consideration\nA court may consider the following factors, among others, in determining whether a limitation or requirement impedes access to abortion services for purposes of subsection (b)(2):\n**(1)**\nWhether the limitation or requirement, in a provider\u2019s good-faith medical judgment, interferes with a health care provider\u2019s ability to provide care and render services, or poses a risk to the patient\u2019s health or safety.\n**(2)**\nWhether the limitation or requirement is reasonably likely to delay or deter a patient in accessing abortion services.\n**(3)**\nWhether the limitation or requirement is reasonably likely to directly or indirectly increase the cost of providing abortion services or the cost for obtaining abortion services such as costs associated with travel, childcare, or time off work.\n**(4)**\nWhether the limitation or requirement is reasonably likely to have the effect of necessitating patient travel that would not otherwise have been required, including by making it necessary for a patient to travel out of State to obtain services.\n**(5)**\nWhether the limitation or requirement is reasonably likely to result in a decrease in the availability of abortion services in a given State or geographic region.\n**(6)**\nWhether the limitation or requirement imposes penalties that are not imposed on other health care providers for comparable conduct or failure to act, or that are more severe than penalties imposed on other health care providers for comparable conduct or failure to act.\n**(7)**\nThe cumulative impact of the limitation or requirement combined with other limitations or requirements.\n##### (d) Exception\nTo defend against a claim that a limitation or requirement violates a health care provider\u2019s or patient\u2019s rights under subsection (b) a party must establish, by clear and convincing evidence, that the limitation or requirement is essential to significantly advance the safety of abortion services or the health of patients and that the safety or health objective cannot be accomplished by a different means that does not interfere with the right protected under subsection (b).\n#### 5. Protection of the right to travel\nA person has a fundamental right under the Constitution of the United States and this Act to travel to a State other than the person\u2019s State of residence, including to obtain reproductive health services such as prenatal, childbirth, fertility, and abortion services, and a person has a right under this Act to assist another person to obtain such services or otherwise exercise the right described in this section.\n#### 6. Applicability and preemption\n##### (a) In general\n**(1) Superseding inconsistent laws**\nExcept as provided under subsection (b), this Act shall supersede any inconsistent Federal or State law, and the implementation of such law, whether statutory, common law, or otherwise, and whether adopted prior to or after the date of enactment of this Act. A Federal or State government official shall not administer, implement, or enforce any law, rule, regulation, standard, or other provision having the force and effect of law that conflicts with any provision of this Act, notwithstanding any other provision of Federal law, including the Religious Freedom Restoration Act of 1993 ( 42 U.S.C. 2000bb et seq. ).\n**(2) Laws after date of enactment**\nFederal law enacted after the date of the enactment of this Act shall be subject to this Act unless such law explicitly excludes such application by reference to this Act.\n##### (b) Limitations\nThe provisions of this Act shall not supersede or apply to\u2014\n**(1)**\nlaws regulating physical access to clinic entrances, such as the Freedom of Access to Clinic Entrances Act of 1994 ( 18 U.S.C. 248 );\n**(2)**\nlaws regulating insurance or medical assistance coverage of abortion services;\n**(3)**\nthe procedure described in section 1531(b)(1) of title 18, United States Code; or\n**(4)**\ngenerally applicable State contract law.\n##### (c) Preemption defense\nIn any legal or administrative action against a person or entity who has exercised or attempted to exercise a right protected by section 4 or section 5 or against any person or entity who has taken any step to assist any such person or entity in exercising such right, this Act shall also apply to, and may be raised as a defense by, such person or entity, in addition to the remedies specified in section 8.\n#### 7. Rules of construction\n##### (a) Liberal construction by courts\nIn any action before a court under this Act, the court shall liberally construe the provisions of this Act to effectuate the purposes of the Act.\n##### (b) Protection of life and health\nNothing in this Act shall be construed to authorize any government official to interfere with, diminish, or negatively affect a person\u2019s ability to obtain or provide abortion services prior to viability, or after viability when, in the good-faith medical judgment of the treating health care provider, continuation of the pregnancy would pose a risk to the pregnant patient\u2019s life or health.\n##### (c) Government officials\nAny person who, by operation of a provision of Federal or State law, including through the grant of a private cause of action, is permitted to implement or enforce a limitation or requirement that violates section 4 or 5 shall be considered a government official for purposes of this Act.\n#### 8. Enforcement\n##### (a) Attorney General\nThe Attorney General may commence a civil action on behalf of the United States in any district court of the United States against any State that violates, or against any government official (including a person described in section 7(c)) who implements or enforces a limitation or requirement that violates, section 4 or 5. The court shall declare unlawful the limitation or requirement if it is determined to be in violation of this Act.\n##### (b) Private right of action\n**(1) In general**\nAny individual or entity adversely affected by an alleged violation of this Act, including any person or health care provider, may commence a civil action against any government official (including a person described in section 7(c)) that implements or enforces a limitation or requirement that violates section 4 or 5. The court shall declare unlawful the limitation or requirement if it is determined to be in violation of this Act.\n**(2) Health care provider**\nA health care provider may commence an action for relief on its own behalf, on behalf of the provider\u2019s staff, and on behalf of the provider\u2019s patients who are or may be adversely affected by an alleged violation of this Act.\n##### (c) Pre-Enforcement challenges\nA suit under subsection (a) or (b) may be brought to prevent enforcement or implementation of a State limitation or requirement that is inconsistent with section 4 or 5.\n##### (d) Declaratory and equitable relief\nIn any action under this section, the court may award appropriate declaratory and equitable relief, including temporary, preliminary, or permanent injunctive relief.\n##### (e) Costs\nIn any action under this section, the court shall award costs of litigation, as well as reasonable attorney\u2019s fees, to any prevailing plaintiff. A plaintiff shall not be liable to a defendant for costs or attorney\u2019s fees in any non-frivolous action under this section.\n##### (f) Jurisdiction\nThe district courts of the United States shall have jurisdiction over proceedings under this Act and shall exercise the same without regard to whether the party aggrieved shall have exhausted any administrative or other remedies that may be provided for by law.\n##### (g) Abrogation of State immunity\nNeither a State that enforces or maintains, nor a government official (including a person described in section 7(c)) who is permitted to implement or enforce any limitation or requirement that violates section 4 or 5 shall be immune under the Tenth Amendment to the Constitution of the United States, the Eleventh Amendment to the Constitution of the United States, or any other source of law, from an action in a Federal or State court of competent jurisdiction challenging that limitation or requirement, unless such immunity is required by clearly established Federal law, as determined by the Supreme Court of the United States.\n#### 9. Effective date\nThis Act shall take effect upon the date of enactment of this Act.\n#### 10. Severability\nIf any provision of this Act, or the application of such provision to any person, entity, government, or circumstance, is held to be unconstitutional, the remainder of this Act, or the application of such provision to all other persons, entities, governments, or circumstances, shall not be affected thereby.",
      "versionDate": "2025-06-24",
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
        "actionDate": "2025-06-24",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "12",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Women\u2019s Health Protection Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-07-15T10:50:40Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2150is.xml"
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
      "title": "Women\u2019s Health Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Women\u2019s Health Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect a person's ability to determine whether to continue or end a pregnancy, and to protect a health care provider's ability to provide abortion services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:22Z"
    }
  ]
}
```
