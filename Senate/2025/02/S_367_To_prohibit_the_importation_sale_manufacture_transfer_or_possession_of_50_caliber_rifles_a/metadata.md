# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/367?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/367
- Title: Stop Arming Cartels Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 367
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2026-01-21T06:51:00Z
- Update date including text: 2026-01-21T06:51:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S546)
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S546)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/367",
    "number": "367",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Stop Arming Cartels Act of 2025",
    "type": "S",
    "updateDate": "2026-01-21T06:51:00Z",
    "updateDateIncludingText": "2026-01-21T06:51:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S546)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-03",
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
          "date": "2025-02-03T22:40:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sponsorshipDate": "2025-02-03",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "HI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "NJ"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "AZ"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "NJ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "AZ"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "CT"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "OR"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "VT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "IL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s367is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 367\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mr. Durbin (for himself, Mr. Blumenthal , Ms. Hirono , Mr. Booker , Mr. Kelly , Mr. Kaine , Mr. Kim , Mr. Gallego , Mr. Murphy , Mr. Reed , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo prohibit the importation, sale, manufacture, transfer, or possession of .50 caliber rifles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Arming Cartels Act of 2025 .\n#### 2. Prohibition on rifles capable of firing .50 caliber ammunition\n##### (a) In general\nChapter 44 of title 18, United States Code, is amended\u2014\n**(1)**\nin section 922, by adding at the end the following:\n(aa) Rifles capable of firing .50 caliber ammunition (1) In general Except as provided in paragraph (2), it shall be unlawful for any person to import, sell, manufacture, transfer, or possess, in or affecting interstate or foreign commerce, a rifle capable of firing .50 caliber ammunition. (2) Exceptions (A) Government use Paragraph (1) shall not apply to the importation for, manufacture for, sale to, transfer to, or possession by the United States, a department or agency of the United States, a State, or a department, agency, or political subdivision of a State, of a rifle capable of firing .50 caliber ammunition. (B) Grandfathered rifles Paragraph (1) shall not apply to the sale, transfer, or possession of any rifle otherwise lawfully possessed on or before the date of enactment of the Stop Arming Cartels Act of 2025 . ; and\n**(2)**\nin section 924(a)(1)(B), by striking or (q) and inserting (q), or (aa) .\n##### (b) Inclusion of certain rifles as firearms under National Firearms Act\n**(1) In general**\nSection 5845(a) of the Internal Revenue Code of 1986 is amended by striking and (8) a destructive device and inserting (8) a destructive device; and (9) a rifle which is capable of firing .50 caliber ammunition and is lawfully possessed on or before the date of enactment of the Stop Arming Cartels Act of 2025 .\n**(2) Effective date**\n**(A) In general**\nSubject to subparagraph (B), the amendments made by this subsection shall take effect on the date which is 12 months after the date of enactment of this Act.\n**(B) Registration**\n**(i) In general**\nNotwithstanding subparagraph (A) or any other provision of law, any person possessing a rifle which is capable of firing .50 caliber ammunition which is not registered to such person in the National Firearms Registration and Transfer Record shall register each such rifle so possessed with the Secretary in such form and manner as the Secretary may require within the 12-month period immediately following the date of enactment of this Act. No fee or tax shall be imposed with respect to any registration required under this subparagraph.\n**(ii) Inclusion in registry**\nAny registration described in clause (i) shall become a part of the National Firearms Registration and Transfer Record. No information or evidence required to be submitted or retained by a natural person to register a firearm under this subparagraph shall be used, directly or indirectly, as evidence against such person in any criminal proceeding with respect to a prior or concurrent violation of law.\n**(C) Definitions**\nIn this paragraph:\n**(i) National Firearms Registration and Transfer Record**\nThe term National Firearms Registration and Transfer Record means the registry established pursuant to section 5841 of the Internal Revenue Code of 1986.\n**(ii) Secretary**\nThe term Secretary has the same meaning given such term under section 7701(a)(11)(B) of the Internal Revenue Code of 1986.\n#### 3. Exception to coverage under Protection of Lawful Commerce in Arms Act\nSection 4(5)(A) of the Protection of Lawful Commerce in Arms Act ( 15 U.S.C. 7903(5)(A) ) is amended\u2014\n**(1)**\nin clause (v), by striking or at the end;\n**(2)**\nin clause (vi), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(vii) an action brought against a manufacturer or seller that knowingly sells or transfers a qualified product, or attempts or conspires to do so, knowing or having reasonable cause to believe that the transaction is prohibited under section 805(c) of the Foreign Narcotics Kingpin Designation Act ( 21 U.S.C. 1904(c) ). .\n#### 4. Federal firearm prohibitor for significant foreign narcotics traffickers and certain other foreign persons\n##### (a) In general\nSection 922(d) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (10), by striking or at the end;\n**(2)**\nby redesignating paragraph (11) as paragraph (12);\n**(3)**\nby inserting after paragraph (10) the following:\n(11) is\u2014 (A) a significant foreign narcotics trafficker publicly identified by the President in a report under subsection (b) or (h)(1) of section 804 of the Foreign Narcotics Kingpin Designation Act ( 21 U.S.C. 1903 ); or (B) a foreign person designated by the Secretary of the Treasury under section 805(b) of the Foreign Narcotics Kingpin Designation Act ( 21 U.S.C. 1904(b) ); or ; and\n**(4)**\nin paragraph (12), as so redesignated, by striking (10) and inserting (11) .\n##### (b) Conforming amendments relating to NICS\nSection 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ) is amended\u2014\n**(1)**\nin subsection (b)(2)(D), by inserting or that transfer of a firearm or ammunition to the individual would violate subsection (d)(11) of such section 922 after section 922 of title 18, United States Code, ;\n**(2)**\nin subsection (e)(1)\u2014\n**(A)**\nin subparagraph (A), by inserting or to whom transfer of a firearm would violate subsection (d)(11) of such section 922, after section 922 of title 18, United States Code or State law, ;\n**(B)**\nin subparagraph (C), by inserting or that transfer of a firearm or ammunition to the person would violate subsection (d)(11) of such section 922, after section 922 of title 18, United States Code, ;\n**(C)**\nin subparagraph (F)(iii)(I), by striking (g) or (n) and inserting (d)(11), (g), or (n) ; and\n**(D)**\nin subparagraph (G)(i), by striking (g) or (n) and inserting (d)(11), (g), or (n) ;\n**(3)**\nin subsection (g), by inserting or that transfer of a firearm to a prospective transferee would violate subsection (d)(11) of such section 922, after section 922 of title 18, United States Code or State law, ; and\n**(4)**\nin subsection (i)(2)\u2014\n**(A)**\nby striking persons, and inserting persons who are ; and\n**(B)**\nby inserting before the period at the end the following: , or to whom transfer of a firearm would violate subsection (d)(11) of such section 922 .\n#### 5. Adding rifles to multiple firearm sales reporting requirements\nSection 923(g)(3)(A) of title 18, United States Code, is amended by striking pistols, or revolvers, or any combination of pistols and revolvers and inserting pistols, revolvers, or rifles, or any combination of pistols, revolvers, and rifles .",
      "versionDate": "2025-02-03",
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
        "actionDate": "2025-02-04",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "923",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop Arming Cartels Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-07T15:24:42Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-04-07T15:24:08Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-04-07T15:24:18Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-04-07T15:24:38Z"
          },
          {
            "name": "Organized crime",
            "updateDate": "2025-04-07T15:24:23Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-04-07T15:24:33Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-04-07T15:24:27Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-04-07T15:24:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-10T15:04:31Z"
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
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s367is.xml"
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
      "title": "Stop Arming Cartels Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Arming Cartels Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the importation, sale, manufacture, transfer, or possession of .50 caliber rifles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:31Z"
    }
  ]
}
```
