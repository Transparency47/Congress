# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2619?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2619
- Title: No Paydays for Hostage-Takers Act
- Congress: 119
- Bill type: HR
- Bill number: 2619
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2026-01-13T09:05:24Z
- Update date including text: 2026-01-13T09:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-09 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-09 - Committee: Ordered to be Reported by the Yeas and Nays: 45 - 6.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-09 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-09 - Committee: Ordered to be Reported by the Yeas and Nays: 45 - 6.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2619",
    "number": "2619",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001322",
        "district": "5",
        "firstName": "Michael",
        "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
        "lastName": "Baumgartner",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "No Paydays for Hostage-Takers Act",
    "type": "HR",
    "updateDate": "2026-01-13T09:05:24Z",
    "updateDateIncludingText": "2026-01-13T09:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 45 - 6.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
        "item": [
          {
            "date": "2025-04-09T14:48:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-03T15:01:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-03T15:01:40Z",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NY"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NV"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "FL"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "GA"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "NJ"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2619ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2619\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Baumgartner (for himself, Mr. Moskowitz , Ms. Tenney , Mr. Amodei of Nevada , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require a report on sanctions under the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Paydays for Hostage-Takers Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Islamic Republic of Iran has a long history of hostage-taking and wrongful detention of United States nationals, including its illegal detention of 52 American diplomats from 1979 to 1981.\n**(2)**\nThe Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741 et seq. ), named in honor of Robert Levinson, the longest-held hostage in United States history who is presumed to have been killed by the regime while in Iranian custody, authorizes sanctions with respect to foreign persons who are responsible for or complicit in hostage-taking or unlawful or wrongful detention of United States nationals abroad.\n#### 3. Statement of policy\nIt shall be the policy of the United States to undertake additional actions and impose strict penalties to deter the Government of Iran and other hostile governments and non-state actors from hostage-taking or wrongfully detaining United States nationals.\n#### 4. Report and certification on restricted Iranian funds released to Qatar\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, and every 180 days thereafter for 6 years, the President shall submit to the Committee on Foreign Affairs and the Committee on Financial Services of the House of Representatives and the Committee on Foreign Relations and the Committee on Banking, Housing, and Urban Affairs of the Senate the following:\n**(1)**\nA report on the $6,000,000,000 in funds transferred from restricted Iranian accounts in the Republic of South Korea to restricted accounts in Qatar on or after August 9, 2023.\n**(2)**\nA certification as to whether credible evidence or intelligence exists that any of the funds transferred have been used for any purpose other than humanitarian purposes.\n**(3)**\nA certification as to whether credible evidence or intelligence exists that the funds transferred have enabled the Government of Iran to increase spending on defense, intelligence, or malign foreign activities.\n##### (b) Matters To be included\nThe report required by subsection (a)(1) shall include the following:\n**(1)**\nAn itemized list of all transactions involving the use of funds transferred, including the value of such transactions, the parties to such transactions, the financial institutions involved, the goods purchased in each transaction, the destinations and end user of such goods, the date on which the United States was notified of such transaction, and the date the transaction occurred.\n**(2)**\nThe quantity of funds described in subsection (a)(1) in restricted accounts in Qatar at the beginning and end of each reporting period.\n**(3)**\nA thorough description of the process the United States Government utilized during the reporting period to review transactions involving the use of funds transferred in order to verify that such transactions were humanitarian in nature.\n#### 5. Review and determination and reports on sanctions under the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act\n##### (a) Review and determination\nNot later than 180 days after the date of the enactment of this Act, and on an annual basis thereafter for 6 years, the President shall\u2014\n**(1)**\nreview all cases of the hostage-taking of a United States national in Iran or at the direction of the Government of Iran and all cases of the unlawful or wrongful detention of a United States national in Iran or at the direction of the Government of Iran that have occurred during the preceding 10-year period; and\n**(2)**\nmake a determination as to whether any foreign person, based on credible evidence\u2014\n**(A)**\nis responsible for or complicit in, or responsible for ordering, controlling, or otherwise directing, the hostage-taking of the United States national or the unlawful or wrongful detention of the United States national; or\n**(B)**\nknowingly provides financial, material, or technological support for, or goods or services in support of, an activity described in subparagraph (A).\n##### (b) Reports\nNot later than 180 days after the date of the enactment of this Act, and on an annual basis thereafter for 6 years, the President shall submit to the appropriate congressional committees a report that\u2014\n**(1)**\nidentifies all foreign persons with respect to which the President has made a determination under subsection (a)(2); and\n**(2)**\nwith respect to each such foreign person\u2014\n**(A)**\nstates whether sanctions have been imposed under section 306 of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741d ) or will be imposed within 30 days of the date of the submission of the report; and\n**(B)**\nfor whom sanctions have not been imposed or will not be imposed under section 306 of such Act, provides a description of the specific authority under which otherwise applicable sanctions are being waived, have otherwise been determined not to apply, or are not being imposed and a complete justification of the decision to waive or otherwise not apply the sanctions authorized by such sanctions programs and authorities.\n#### 6. Requirement to limit travel of Iranian diplomats at the United Nations\n##### (a) Findings\nCongress finds the following:\n**(1)**\nUnited States visa restrictions on sanctioned individuals often contain exceptions for activities in order to permit the United States to comply with the Agreement regarding the headquarters of the United Nations signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States.\n**(2)**\nSection 6 of Public Law 80\u2013357 (commonly known as the United Nations Headquarters Agreement Act ) provides Nothing in the agreement shall be construed as in any way diminishing, abridging, or weakening the right of the United States to safeguard its own security. .\n**(3)**\nCongress has directed the President to use the President\u2019s authority, including the authorities contained in section 6 of Public Law 80\u2013357 , to deny any individual\u2019s admission to the United States as a representative to the United Nations if the President determines that such individual has been found to have been engaged in espionage activities or a terrorist activity directed against the United States or its allies and may pose a threat to United States national security interests.\n##### (b) Sense of congress\nIt is the sense of Congress that Iran\u2019s longstanding hostage-taking and wrongful detention of United States nationals, assassination plots against United States nationals outside and within the United States, and intelligence activities are a security or terrorist threat to the United States and United States interests and shall be a primary consideration in limiting travel of Iranian diplomats seeking admission to the United States for United Nations activities and their family members.\n##### (c) Denial of visas\nSection 407(a)(1) of the Foreign Relations Authorization Act, Fiscal Years 1990 and 1991 ( 8 U.S.C. 1102 note) is amended\u2014\n**(1)**\nby striking (1) and inserting (1)(A) ;\n**(2)**\nby striking and at the end and inserting or ; and\n**(3)**\nby adding further at the end the following:\n(B) has been sanctioned pursuant to Executive Order 13224 (66 Fed. Reg. 49079; relating to blocking property and prohibiting transactions with persons who commit, threaten to commit, or support terrorism) or Executive Order 13382 (70 Fed. Reg. 38567; relating to blocking property of weapons of mass destruction proliferators and their supporters) as of the date of the enactment of the No Paydays for Hostage-Takers Act; and .\n##### (d) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 3 years, the President shall submit to the appropriate congressional committees a report on whether the President has taken action to restrict the travel of Iranian diplomats seeking admission to the United States for United Nations activities and their family members and identifying each such instance in which visas were denied or travel was restricted.\n#### 7. Report on blocked Iranian assets\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 3 years, the President shall submit to the appropriate congressional committees a report that includes the following:\n**(1)**\nAn itemized list of any identifiable assets with a valuation of more than $100,000 belonging to Iranian individuals and entities that are or have been blocked or otherwise frozen pursuant to any sanctions program under any jurisdiction globally, in the prior 2 years.\n**(2)**\nAny changes to the status of such assets, including unblocking, unfreezing, or transferring such assets, in the prior 2 years.\n**(3)**\nWith respect to any changes identified in paragraph (2), whether the United States Government took any action, including waiving of sanctions, that related to such unblocking or unfreezing, and a justification for any such United States actions.\n#### 8. Report on international efforts to freeze and seize Iranian assets\n##### (a) Sense of congress\nIt is the sense of Congress that the Secretary of State, the Secretary of the Treasury, and the Attorney General should, to the extent practicable\u2014\n**(1)**\ncarry out a coordinated international effort to find, restrain, freeze, and where appropriate and legally authorized, seize, confiscate or forfeit the assets of those individuals and entities that have been sanctioned in connection with Iran\u2019s malign activities, including hostage-taking, wrongful detention, and human rights violations; and\n**(2)**\nwork with foreign governments\u2014\n**(A)**\nto share intelligence of financial investigations, as appropriate;\n**(B)**\nto oversee the assets identified pursuant to paragraph (1); and\n**(C)**\nto provide technical assistance to help governments establish the necessary legal framework to carry out asset forfeitures.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 3 years, the President shall submit to the appropriate congressional committees a report on actions described in subsection (a).\n#### 9. Determination and report on invalidating United States passports for travel to Iran\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe Secretary of State maintains authority to restrict the use of United States passports for travel to or use in a country or area which the Secretary has determined is a country or area in which there is imminent danger to the public health or physical safety of United States travelers, in accordance with section 51.63 of title 22, Code of Federal Regulations.\n**(2)**\nIn 2017, the Secretary of State declared United States passports invalid for travel to, in, or through North Korea, unless specially validated for such travel, after United States citizen Otto Warmbier suffered grievous injuries in North Korean custody, which led to his death.\n**(3)**\nThe ban on use of United States passports for travel to North Korea was renewed in 2023.\n##### (b) Sense of congress\nIt is the sense of Congress that the Secretary of State should declare United States passports invalid for travel to, in, or through Iran due to the imminent danger to the public health and physical safety of United States travelers stemming from the threat of wrongful detention or being taken hostage by the Iranian regime.\n##### (c) Determination and report\nNot later than 90 days after the date of enactment of this Act and annually thereafter for 3 years, the Secretary of State shall determine and report to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate\u2014\n**(1)**\nwhether the travel of United States persons to Iran presents an imminent danger to the public health or physical safety of United States travelers; and\n**(2)**\nwhether the Secretary is exercising his authority to declare United States passports invalid for travel to, in, or through Iran.\n#### 10. Strategy to deter hostage-taking\nNot later than 180 days after the date of the enactment of this Act, the President shall develop and submit to Congress a strategy to deter and prevent wrongful detention and hostage-taking by United States adversaries, including identifying penalties for wrongful detention and hostage-taking, identifying clear United States Government policies barring the payment of ransom or transactions that could be viewed as ransom by the United States Government, and detailing plans to coordinate with United States allies and partners on such strategy.\n#### 11. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nthe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs and the Committee on the Judiciary of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on the Judiciary of the Senate.\n**(2) Foreign person**\nThe term foreign person \u2014\n**(A)**\nmeans an individual or entity that is not a United States person; and\n**(B)**\nincludes a foreign state (as such term is defined in section 1603 of title 28, United States Code).\n**(3) United states national**\nThe term United States national has the meaning given that term in section 307(2) of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741e(2) ).",
      "versionDate": "2025-04-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Arms control and nonproliferation",
            "updateDate": "2025-06-10T17:33:22Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-06-10T17:33:23Z"
          },
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2025-06-10T17:33:23Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-10T17:33:23Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-06-10T17:33:22Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-06-10T17:33:22Z"
          },
          {
            "name": "Foreign and international banking",
            "updateDate": "2025-06-10T17:33:23Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-06-10T17:33:23Z"
          },
          {
            "name": "Iran",
            "updateDate": "2025-06-10T17:33:22Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2025-06-10T17:33:22Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-06-10T17:33:22Z"
          },
          {
            "name": "Qatar",
            "updateDate": "2025-06-10T17:33:22Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-06-10T17:33:22Z"
          },
          {
            "name": "South Korea",
            "updateDate": "2025-06-10T17:33:23Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-06-10T17:33:22Z"
          },
          {
            "name": "Travel and tourism",
            "updateDate": "2025-06-10T17:33:23Z"
          },
          {
            "name": "United Nations",
            "updateDate": "2025-06-10T17:33:22Z"
          },
          {
            "name": "Visas and passports",
            "updateDate": "2025-06-10T17:33:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-23T13:34:59Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2619ih.xml"
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
      "title": "No Paydays for Hostage-Takers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Paydays for Hostage-Takers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a report on sanctions under the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T04:18:20Z"
    }
  ]
}
```
