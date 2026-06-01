# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8168?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8168
- Title: Major Non-NATO Ally Terror Threat Assessment Act
- Congress: 119
- Bill type: HR
- Bill number: 8168
- Origin chamber: House
- Introduced date: 2026-03-30
- Update date: 2026-05-16T08:07:00Z
- Update date including text: 2026-05-16T08:07:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-30: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-31 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.
- Latest action: 2026-03-30: Introduced in House

## Actions

- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Introduced in House
- 2026-03-30 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-31 - Committee: Referred to the Subcommittee on Counterterrorism and Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-30",
    "latestAction": {
      "actionDate": "2026-03-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8168",
    "number": "8168",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "V000139",
        "district": "7",
        "firstName": "Matt",
        "fullName": "Rep. Van Epps, Matt [R-TN-7]",
        "lastName": "Van Epps",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Major Non-NATO Ally Terror Threat Assessment Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:00Z",
    "updateDateIncludingText": "2026-05-16T08:07:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-31",
      "committees": {
        "item": {
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Counterterrorism and Intelligence.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-30",
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
      "actionDate": "2026-03-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-30",
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
          "date": "2026-03-30T16:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-31T04:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Counterterrorism, Law Enforcement, and Intelligence Subcommittee",
          "systemCode": "hshm05"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8168ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8168\nIN THE HOUSE OF REPRESENTATIVES\nMarch 30, 2026 Mr. Van Epps introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo require an assessment of terrorism threats to the United States posed by foreign terrorist organizations and Specially Designated Global Terrorists present in countries that are major non-NATO allies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Major Non-NATO Ally Terror Threat Assessment Act .\n#### 2. Assessment of terrorism threats to the United States by foreign terrorist organizations and Specially Designated Global Terrorists present in countries that are major non-NATO allies\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act and biennially thereafter, the Secretary of Homeland Security, in consultation with the Secretary of State and the Director of National Intelligence, shall submit to the appropriate congressional committees an assessment of terrorism threats to the United States posed by foreign terrorist organizations and Specially Designated Global Terrorists present in countries operating or designated as major non-NATO allies.\n##### (b) Elements\nEach assessment of terrorism threats required under subsection (a) shall include the following for each major non-NATO ally:\n**(1)**\nAn identification of each foreign terrorist organization or Specially Designated Global Terrorist present in each such ally.\n**(2)**\nA description of all activities in which each such identified foreign terrorist organization or Specially Designated Global Terrorist is engaged within each such ally, including the extent to which the each such identified foreign terrorist organization or Specially Designated Global Terrorist is using artificial intelligence or critical and emerging technologies.\n**(3)**\nA description of efforts of the government of each such MNNA ally to disrupt and degrade the activities of each such identified foreign terrorist organization or Specially Designated Global Terrorist within such ally, including any cooperation with elements of the United States intelligence community.\n**(4)**\nAn assessment of the capability of the Department of Homeland Security to identify, monitor, and mitigate terrorist threats to the United States by each such identified foreign terrorist organization or Specially Designated Global Terrorist present in each such MNNA ally.\n**(5)**\nAn assessment of the capability of the Department of Homeland Security to prevent individuals who are members of any such identified foreign terrorist organization or Specially Designated Global Terrorist in each such MNNA ally from entering the United States.\n**(6)**\nAn identification of any additional resources required to counter terror threats to the United States posed by each such identified foreign terrorist organization or Specially Designated Global Terrorist present in each such MNNA ally.\n##### (c) Form and further availability\nEach assessment of terrorism threats required under subsection (a) shall be submitted in classified form and be made available to every Member of Congress, upon request.\n##### (d) Congressional briefing\nUpon submission of each assessment of terrorism threats required under subsection (a), the Secretary of Homeland Security shall provide to the appropriate congressional committees a briefing on such assessment.\n##### (e) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate.\n**(2) Artificial intelligence**\nThe term artificial intelligence has the meaning given such term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(3) Critical and emerging technologies**\nThe term critical and emerging technologies means those technologies listed in the February 2024 Critical and Emerging Technologies List Update issued by the National Science and Technology Council (NSTC), or any successor thereto.\n**(4) Intelligence community**\nThe term intelligence community has the meaning given such term in section 3(4) of the National Security Act of 1947 ( 50 U.S.C. 3003(4) ).\n**(5) Foreign terrorist organization**\nThe term foreign terrorist organization means an organization designated as a foreign terrorist organization pursuant to section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ).\n**(6) Major non-NATO ally**\nThe term major non-NATO ally has the meaning given such term in section 644 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2403 ).\n**(7) Specially designated global terrorist**\nThe term specially designated global terrorist means individuals or organizations designated as a specially designated global terrorist pursuant Executive Order 13224 (entitled Blocking Property and Prohibiting Transactions With Persons Who Commit, Threaten To Commit, or Support Terrorism ; September 23, 2001; 66 Fed. Reg. 49079).\n**(8) Terrorism**\nThe term terrorism has the meaning given such term in section 2 of the Homeland Security Act of 2002 ( 6 U.S.C. 101 ).",
      "versionDate": "2026-03-30",
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
        "name": "International Affairs",
        "updateDate": "2026-04-13T21:11:58Z"
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
      "date": "2026-03-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8168ih.xml"
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
      "title": "Major Non-NATO Ally Terror Threat Assessment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Major Non-NATO Ally Terror Threat Assessment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require an assessment of terrorism threats to the United States posed by foreign terrorist organizations and Specially Designated Global Terrorists present in countries that are major non-NATO allies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:47Z"
    }
  ]
}
```
