# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/825?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/825
- Title: Fighting Post-Traumatic Stress Disorder Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 825
- Origin chamber: Senate
- Introduced date: 2025-03-04
- Update date: 2026-05-22T02:23:25Z
- Update date including text: 2026-05-22T02:23:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-04: Introduced in Senate
- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported with amendments favorably.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2026-05-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 411.
- Latest action: 2025-03-04: Introduced in Senate

## Actions

- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported with amendments favorably.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.
- 2026-05-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 411.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/825",
    "number": "825",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Fighting Post-Traumatic Stress Disorder Act of 2025",
    "type": "S",
    "updateDate": "2026-05-22T02:23:25Z",
    "updateDateIncludingText": "2026-05-22T02:23:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 411.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with amendments favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-03-04",
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
        "item": [
          {
            "date": "2026-05-19T18:51:55Z",
            "name": "Reported By"
          },
          {
            "date": "2026-05-14T17:58:12Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-04T15:30:43Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-04T15:30:43Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "DE"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "IN"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NH"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "MO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "CT"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "TN"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "IA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "SC"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NV"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "MN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "NC"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "HI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "VT"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s825is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 825\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mr. Grassley (for himself, Mr. Coons , Mr. Young , Ms. Hassan , Mr. Hawley , Mr. Blumenthal , Mrs. Blackburn , Mr. Ossoff , Ms. Ernst , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Attorney General to propose a program for making treatment for post-traumatic stress disorder and acute stress disorder available to public safety officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fighting Post-Traumatic Stress Disorder Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPublic safety officers serve their communities with bravery and distinction in order to keep their communities safe.\n**(2)**\nPublic safety officers, including police officers, firefighters, emergency medical technicians, and 911 dispatchers, are on the front lines of dealing with situations that are stressful, graphic, harrowing, and life-threatening.\n**(3)**\nThe work of public safety officers puts them at risk for developing post-traumatic stress disorder and acute stress disorder.\n**(4)**\nIt is estimated that 30 percent of public safety officers develop behavioral health conditions at some point in their lifetimes, including depression and post-traumatic stress disorder, in comparison to 20 percent of the general population that develops such conditions.\n**(5)**\nVictims of post-traumatic stress disorder and acute stress disorder are at a higher risk of dying by suicide.\n**(6)**\nFirefighters have been reported to have higher suicide attempt and ideation rates than the general population.\n**(7)**\nIt is estimated that between 125 and 300 police officers die by suicide every year.\n**(8)**\nIn 2019, pursuant to section 2(b) of the Law Enforcement Mental Health and Wellness Act of 2017 ( Public Law 115\u2013113 ; 131 Stat. 2276), the Director of the Office of Community Oriented Policing Services of the Department of Justice developed a report (referred to in this section as the LEMHWA report ) that expressed that many law enforcement agencies do not have the capacity or local access to the mental health professionals necessary for treating their law enforcement officers.\n**(9)**\nThe LEMHWA report recommended methods for establishing remote access or regional mental health check programs at the State or Federal level.\n**(10)**\nIndividual police and fire departments generally do not have the resources to employ full-time mental health experts who are able to treat public safety officers with state-of-the-art techniques for the purpose of treating job-related post-traumatic stress disorder and acute stress disorder.\n#### 3. Programming for post-traumatic stress disorder\n##### (a) Definitions\nIn this section:\n**(1) Public safety officer**\nThe term public safety officer \u2014\n**(A)**\nhas the meaning given the term in section 1204 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 ); and\n**(B)**\nincludes Tribal public safety officers.\n**(2) Public safety telecommunicator**\nThe term public safety telecommunicator means an individual who\u2014\n**(A)**\noperates telephone, radio, or other communication systems to receive and communicate requests for emergency assistance at 911 public safety answering points and emergency operations centers;\n**(B)**\ntakes information from the public and other sources relating to crimes, threats, disturbances, acts of terrorism, fires, medical emergencies, and other public safety matters; and\n**(C)**\ncoordinates and provides information to law enforcement and emergency response personnel.\n##### (b) Report\nNot later than 150 days after the date of enactment of this Act, the Attorney General, acting through the Director of the Office of Community Oriented Policing Services of the Department of Justice, shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on\u2014\n**(1)**\nnot fewer than 1 proposed program, if the Attorney General determines it appropriate and feasible to do so, to be administered by the Department of Justice for making state-of-the-art treatments or preventative care available to public safety officers and public safety telecommunicators with regard to job-related post-traumatic stress disorder or acute stress disorder by providing public safety officers and public safety telecommunicators access to evidence-based trauma-informed care, peer support, counselor services, and family supports for the purpose of treating or preventing post-traumatic stress disorder or acute stress disorder;\n**(2)**\na draft of any necessary grant conditions required to ensure that confidentiality is afforded to public safety officers on account of seeking the care or services described in paragraph (1) under the proposed program;\n**(3)**\nhow each proposed program described in paragraph (1) could be most efficiently administered throughout the United States at the State, Tribal, territorial, and local levels, taking into account in-person and telehealth capabilities;\n**(4)**\na draft of legislative language necessary to authorize each proposed program described in paragraph (1); and\n**(5)**\nan estimate of the amount of annual appropriations necessary for administering each proposed program described in paragraph (1).\n##### (c) Development\nIn developing the report required under subsection (b), the Attorney General shall consult relevant stakeholders, including\u2014\n**(1)**\nFederal, State, Tribal, territorial, and local agencies employing public safety officers and public safety telecommunicators; and\n**(2)**\nnon-governmental organizations, international organizations, academies, or other entities, including organizations that support the interests of public safety officers and public safety telecommunicators and the interests of family members of public safety officers and public safety telecommunicators.",
      "versionDate": "2025-03-04",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s825rs.xml",
      "text": "II\nCalendar No. 411\n119th CONGRESS\n2d Session\nS. 825\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mr. Grassley (for himself, Mr. Coons , Mr. Young , Ms. Hassan , Mr. Hawley , Mr. Blumenthal , Mrs. Blackburn , Mr. Ossoff , Ms. Ernst , Mr. Warnock , Mrs. Gillibrand , Mr. Graham , Ms. Cortez Masto , Mr. Durbin , Ms. Klobuchar , Mr. Tillis , Ms. Hirono , Mr. Padilla , Mr. Welch , and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 19, 2026 Reported by Mr. Grassley , with amendments Omit the parts struck through and insert the part printed in italic\nA BILL\nTo require the Attorney General to propose a program for making treatment for post-traumatic stress disorder and acute stress disorder available to public safety officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fighting Post-Traumatic Stress Disorder Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPublic safety officers serve their communities with bravery and distinction in order to keep their communities safe.\n**(2)**\nPublic safety officers, including police officers, firefighters, emergency medical technicians, and 911 dispatchers, are on the front lines of dealing with situations that are stressful, graphic, harrowing, and life-threatening.\n**(3)**\nThe work of public safety officers puts them at risk for developing post-traumatic stress disorder and acute stress disorder.\n**(4)**\nIt is estimated that 30 percent of public safety officers develop behavioral health conditions at some point in their lifetimes, including depression and post-traumatic stress disorder, in comparison to 20 percent of the general population that develops such conditions.\n**(5)**\nVictims of post-traumatic stress disorder and acute stress disorder are at a higher risk of dying by suicide.\n**(6)**\nFirefighters have been reported to have higher suicide attempt and ideation rates than the general population.\n**(7)**\nIt is estimated that between 125 and 300 police officers die by suicide every year.\n**(8)**\nIn 2019, pursuant to section 2(b) of the Law Enforcement Mental Health and Wellness Act of 2017 ( Public Law 115\u2013113 ; 131 Stat. 2276), the Director of the Office of Community Oriented Policing Services of the Department of Justice developed a report (referred to in this section as the LEMHWA report ) that expressed that many law enforcement agencies do not have the capacity or local access to the mental health professionals necessary for treating their law enforcement officers.\n**(9)**\nThe LEMHWA report recommended methods for establishing remote access or regional mental health check programs at the State or Federal level.\n**(10)**\nIndividual police and fire departments generally do not have the resources to employ full-time mental health experts who are able to treat public safety officers with state-of-the-art techniques for the purpose of treating job-related post-traumatic stress disorder and acute stress disorder.\n#### 3. Programming for post-traumatic stress disorder\n##### (a) Definitions\nIn this section:\n**(1) Public safety officer**\nThe term public safety officer \u2014\n**(A)**\nhas the meaning given the term in section 1204 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 ); and\n**(B)**\nincludes Tribal public safety officers.\n**(2) Public safety telecommunicator**\nThe term public safety telecommunicator means an individual who\u2014\n**(A)**\noperates telephone, radio, or other communication systems to receive and communicate requests for emergency assistance at 911 public safety answering points and emergency operations centers;\n**(B)**\ntakes information from the public and other sources relating to crimes, threats, disturbances, acts of terrorism, fires, medical emergencies, and other public safety matters; and\n**(C)**\ncoordinates and provides information to law enforcement and emergency response personnel.\n##### (b) Report\nNot later than 150 days after the date of enactment of this Act, the Attorney General, acting through the Director of the Office of Community Oriented Policing Services of the Department of Justice, shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on\u2014\n**(1)**\nnot fewer than 1 proposed program, if the Attorney General determines it appropriate and feasible to do so, to be administered by the Department of Justice for making state-of-the-art treatments or preventative care available to public safety officers and public safety telecommunicators with regard to job-related post-traumatic stress disorder or acute stress disorder by providing public safety officers and public safety telecommunicators access to evidence-based trauma-informed care, peer support, counselor services, and family supports for the purpose of treating or preventing post-traumatic stress disorder or acute stress disorder;\n**(2)**\na draft of any necessary grant conditions required to ensure that confidentiality is afforded to public safety officers on account of seeking the care or services described in paragraph (1) under the proposed program;\n**(3)**\nhow each proposed program described in paragraph (1) could be most efficiently administered throughout the United States at the State, Tribal, territorial, and local levels, taking into account in-person and telehealth capabilities;\n**(4)**\na draft of legislative language necessary to authorize each proposed program described in paragraph (1); and\n**(5)**\nan estimate of the amount of annual appropriations necessary for administering each proposed program described in paragraph (1).\n##### (c) Development\nIn developing the report required under subsection (b), the Attorney General shall consult relevant stakeholders, including\u2014\n**(1)**\nFederal, State, Tribal, territorial, and local agencies employing public safety officers and public safety telecommunicators; and\n**(2)**\nnon - governmental organizations, international organizations, academies, or other entities, including organizations that support the interests of public safety officers , and public safety telecommunicators , and the interests of family members of public safety officers and public safety telecommunicators.",
      "versionDate": "2026-05-19",
      "versionType": "Reported in Senate"
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
        "updateDate": "2025-03-26T14:25:45Z"
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
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s825is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s825rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Fighting Post-Traumatic Stress Disorder Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-22T02:23:25Z"
    },
    {
      "title": "Fighting Post-Traumatic Stress Disorder Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fighting Post-Traumatic Stress Disorder Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Attorney General to propose a program for making treatment for post-traumatic stress disorder and acute stress disorder available to public safety officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:41Z"
    }
  ]
}
```
