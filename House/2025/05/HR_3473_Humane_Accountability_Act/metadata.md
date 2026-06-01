# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3473?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3473
- Title: Humane Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 3473
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-05-22T08:08:54Z
- Update date including text: 2026-05-22T08:08:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-16 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-16 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3473",
    "number": "3473",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Humane Accountability Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:54Z",
    "updateDateIncludingText": "2026-05-22T08:08:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-16",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-16T04:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-15T14:05:45Z",
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "IL"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "IL"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
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
      "sponsorshipDate": "2025-08-12",
      "state": "OH"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "MI"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "OR"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3473ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3473\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Vasquez (for himself, Ms. Budzinski , and Mr. Vargas ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require a report on detainees in the custody of U.S. Customs and Border Protection, U.S. Immigration and Customs Enforcement, or the Office of Refugee Resettlement (ORR), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Humane Accountability Act .\n#### 2. Reports relating to certain detainees\n##### (a) Information to Congress\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Homeland Security shall submit to Congress a report containing information relating to the following:\n**(1)**\nThe number of U.S. Customs and Border Protection (CBP) and U.S. Immigration and Customs Enforcement (ICE) encounters that have occurred since January 21, 2025, that have resulted in the detention of a noncitizen, including the names and nationalities of the individuals affected and an identification of the legal or other authority under which each such detention occurred.\n**(2)**\nThe number of CBP and ICE encounters that have occurred since January 21, 2025, at sensitive or protected locations, including schools, places of worship, hospitals, child care centers, courthouses, and other locations where minor children may be present.\n**(3)**\nThe total number of removals that have occurred since January 21, 2025, including the names, nationalities, and alien numbers of the individuals affected, an identification of the legal or other authority under which each such removal occurred, and an identification of the countries to which such individuals were removed.\n**(4)**\nThe names and nationalities of any noncitizens who have been removed to the Terrorism Confinement Center (CECOT) in El Salvador or to Guantanamo Bay, including those who were not subject to a final order of removal.\n##### (b) Report on DHS and HHS detainees\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Homeland Security and the Secretary of Health and Human Services shall jointly submit to Congress and the Comptroller General of the United States a report regarding detainees in the custody of U.S. Customs and Border Protection (CBP), U.S. Immigration and Customs Enforcement (ICE), or the Office of Refugee Resettlement (ORR), as the case may be. Such report shall include information relating to the following:\n**(A)**\nAll instances of assault or abuse against detainees while in custody either by an officer, staff, or other detainee that requires medical attention.\n**(B)**\nAll reports of sexual assault on detainees while in custody, as well as any findings from subsequent investigations into each such assault.\n**(C)**\nAll reports of instances of local law enforcement being called to a facility, including emergency responders.\n**(D)**\nAll reports of instances in which a detainee was transferred from a facility for medical care requiring overnight hospitalization.\n**(E)**\nAll instances of detainee deaths while in custody.\n**(F)**\nThe frequency and topic of complaints submitted to authorities at detention centers by detainees or their families regarding abuse, sexual assault, staff neglect, staff retaliation, lack of proper resources or amenities, or deaths, as well as any action taken by such authorities to address and remedy such complaints.\n**(G)**\nThe frequency of complaints submitted by detainees or their families relating to lack of access to legal counsel as well as any action taken by such authority to address and remedy such complaints.\n**(2) GAO recommendations**\nNot later than 90 days after receipt of the report required under paragraph (1), the Comptroller General of the United States shall submit to Congress a list of recommendations to address the instances, reports, and complaints included in such report, as well as additional recommendations relating to the following:\n**(A)**\nThe effects of closures of the United States Citizenship and Immigration Services (USCIS) Ombudsman, the Office for Civil Rights and Civil Liberties (CRCL) of the Department of Homeland Security, and the Immigration Detention Ombudsman (OIDO) of the Department of Homeland Security on the ability to file reports of assaults, abuse, or improper actions against those in the custody of the Department of Homeland Security or the Department of Health and Human Services, as the case may be.\n**(B)**\nEnsuring compliance with all applicable legal visitation and access requirements.\n**(C)**\nEnsuring the Offices of the Inspectors General or the Department of Homeland Security and the Department of Health and Human Services increase regular reviews of detention facilities and compliance with all applicable due process and civil rights protections.\n**(D)**\nImproving the process for tracking the location of detainees while in custody, including making publicly available information related to current location of such detainees, all transfers to facilities operated or controlled by the Department of Homeland Security or the Office of Refugee Resettlement of the Department of Health and Human Services, as the case may be, throughout the entirety of the relevant removal process, and ensuring the ICE Online Detainee Locator System reflects the final repatriation location for individuals who have been removed.\n##### (c) Notice relating to detention at non-Tradition locations\n**(1) In general**\nNot later than 60 days before the Secretary of Homeland Security or the Secretary of Health and Human Services plans to utilize a non-traditional location described in paragraph (3) for the detention of a detainee (including a non-citizen minor or family unit) in the custody of U.S. Customs and Border Protection (CBP), U.S. Immigration and Customs Enforcement (ICE), or the Office of Refugee Resettlement (ORR) of the Department of Health and Human Services, as the case may be, the Secretary of Homeland Security or the Secretary of Health and Human Services, as appropriate, shall, in coordination with the Attorney General, the Secretary of Defense, and the head of any other relevant Federal department or agency, submit to Congress a notification regarding such plans.\n**(2) Elements**\nA notification under paragraph (1) shall also include information relating to the following:\n**(A)**\nThe type and specific location for the nontraditional detention location.\n**(B)**\nA justification for utilization.\n**(C)**\nThe number of detention beds that will be utilized.\n**(D)**\nDetails of efforts to ensure compliance with all reporting, access, and due process requirements.\n**(E)**\nA copy of detention standard of care that will be applied, including facilitation of access to medical services.\n**(F)**\nA timeline, estimated costs, budget, and utilized funds.\n**(G)**\nA copy of any agreements for use of the nontraditional location, including a record of any funding or proposed payments.\n**(3) Non-traditional locations described**\nA non-traditional location described in this paragraph is any of the following:\n**(A)**\nAny building, grounds, or property under the jurisdiction, custody, or control of the Department of Defense.\n**(B)**\nAny building, grounds, or property located on Indian lands (as such term is defined in section 502.12 of title 25, Code of Federal Regulations).\n**(C)**\nAny lands outside the external boundary of the continental United States.",
      "versionDate": "2025-05-15",
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
        "name": "Immigration",
        "updateDate": "2025-05-29T14:02:56Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3473ih.xml"
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
      "title": "Humane Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:53Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Humane Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a report on detainees in the custody of U.S. Customs and Border Protection, U.S. Immigration and Customs Enforcement, or the Office of Refugee Resettlement (ORR), and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:46Z"
    }
  ]
}
```
