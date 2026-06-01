# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3798?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3798
- Title: Safe Access to Cash Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3798
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-05-01T18:55:44Z
- Update date including text: 2026-05-01T18:55:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-03-05 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-03-05 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-03-05 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-03-05 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 350.
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-03-05 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-03-05 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-03-05 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-03-05 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 350.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3798",
    "number": "3798",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Safe Access to Cash Act of 2026",
    "type": "S",
    "updateDate": "2026-05-01T18:55:44Z",
    "updateDateIncludingText": "2026-05-01T18:55:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 350.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-03-05",
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
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-05",
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
      "actionDate": "2026-02-05",
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
            "date": "2026-03-05T19:22:01Z",
            "name": "Reported By"
          },
          {
            "date": "2026-03-05T16:00:24Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-05T19:50:14Z",
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "AZ"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3798is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3798\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Mr. Cruz (for himself and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish criminal offenses with respect to violations involving ATMs, regardless of whether the ATM is located on the physical premises of a financial institution, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Access to Cash Act of 2026 .\n#### 2. Offenses related to ATM robbery and incidental crimes\n##### (a) In general\nChapter 103 of title 18, United States Code, is amended by inserting after section 2113 the following:\n2113A. ATM robbery and incidental crimes (a) Offenses against ATM users and servicers Whoever, by force or violence, or by intimidation, takes, or attempts to take, or conspires to take, any property or money or any other thing of value from any person using or servicing, or attempting to use or service, an ATM, or from any person having used or serviced an ATM, where the offense is committed in connection with such use or service, or from any owner or operator of any network-connected ATM while such person is engaged in transporting or delivering property that is to be inserted into any such ATM, or from any person engaged in such transport or delivery under contract with, or employment by, any such owner or operator, or who extorts or attempts or conspires to obtain by extortion, any property or money or any other thing of value from any such person described in this subsection, shall be fined under this title or imprisoned not more than 20 years, or both. (b) Offenses against property (1) Offenses exceeding $1,000 Whoever breaks into, tampers with, damages, removes, steals, or attempts to break into, tamper with, damage, remove, or steal any ATM without authorization of the owner or operator of any such ATM, and removes or attempts to remove any property or money from any such ATM exceeding $1,000, shall be fined under this title or imprisoned not more than 10 years, or both. (2) Offenses not exceeding $1,000 Whoever breaks into, tampers with, damages, removes, steals, or attempts to break into, tamper with, damage, remove, or steal any ATM without authorization of the owner or operator of any such ATM, and does not remove or attempt to remove any property or money from any such ATM exceeding $1,000, shall be fined under this title or imprisoned not more than 1 year, or both. (c) Receipt, possession, concealment, storage, barter, sale, or disposal of property acquired unlawfully under this section Whoever receives, possesses, conceals, stores, barters, sells, or disposes of, any property or money or other thing of value that has been taken in violation of subsection (a) or (b), or conspires to do so, knowing the same to be property that has been unlawfully taken, shall be subject to the punishment provided in subsection (a) or (b), as applicable, for the taker. (d) Assault in connection with offenses Whoever, in committing, or in attempting to commit, any offense defined in subsection (a) or (b), forcibly assaults any person, or puts in jeopardy the life of any person by the use of a dangerous weapon or device, shall be fined under this title or imprisoned not more than 25 years, or both. (e) Killing or forcible accompaniment in connection with offenses Whoever, in committing any offense defined in this section, or in avoiding or attempting to avoid apprehension for the commission of such offense, or in freeing himself or attempting to free himself from arrest or confinement for such offense, kills any person, or forces any person to accompany the offender without the consent of such person, shall be imprisoned not less than 10 years, or, if death results, shall be punished by life imprisonment. (f) Definitions In this section: (1) ATM The term ATM \u2014 (A) means any network-connected automated teller machine terminal that is connected to 1 or more of the global, national, or regional electronic financial networks that allow a depositor of any bank, credit union, or savings and loan association, by use at such automated teller machine of a card or other access device, as defined in section 1029(e)(1), issued or authorized by such depository institution, to access the account of the depositor for the purpose of making withdrawals from or deposits to such account, or making inquiry as to the balance in such account; and (B) includes any automated teller machine owned, operated, or sponsored by a bank, credit union, or any savings and loan association, regardless of whether\u2014 (i) the automated teller machine is located on the physical premises of such an institution; or (ii) the automated teller machine is owned or operated by such an institution. (2) Bank; credit union; savings and loan association The terms bank , credit union , and savings and loan association have the meanings given those terms in section 2113. (3) Extortion The term extortion has the meaning given the term in section 1951(b)(2). (g) Included offenses The offenses defined in subsections (a) and (b) include any such offense committed against or involving an ATM, or any person using or servicing, or attempting to use or service, or against a person having used or serviced an ATM, where the offense is committed in connection with, or by reason of, such use or service, and any such offense against any owner or operator of an ATM while such person is engaged in transporting or delivering property that is to be loaded into an ATM, or against any person engaged in such transport or delivery under contract with, or employment by, any such owner or operator. .\n##### (b) Clerical amendment\nThe table of sections for chapter 103 of title 18, United States Code, is amended by inserting after the item relating to section 2113 the following:\n2113A. ATM robbery and incidental crimes. .\n#### 3. Offenses related to bank robbery and incidental crimes\nSection 2113(a) of title 18, United States Code, is amended\u2014\n**(1)**\nin the first paragraph, by striking force and violence and inserting force or violence ; and\n**(2)**\nby inserting or conspires to take, before from the person or presence of another, .",
      "versionDate": "2026-02-05",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3798rs.xml",
      "text": "II\nCalendar No. 350\n119th CONGRESS\n2d Session\nS. 3798\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Mr. Cruz (for himself, Mr. Gallego , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMarch 5, 2026 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend title 18, United States Code, to establish criminal offenses with respect to violations involving ATMs, regardless of whether the ATM is located on the physical premises of a financial institution, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Access to Cash Act of 2026 .\n#### 2. Offenses related to ATM robbery and incidental crimes\n##### (a) In general\nChapter 103 of title 18, United States Code, is amended by inserting after section 2113 the following:\n2113A. ATM robbery and incidental crimes (a) Offenses against ATM users and servicers Whoever, by force or violence, or by intimidation, takes, or attempts to take, or conspires to take, any property or money or any other thing of value from any person using or servicing, or attempting to use or service, an ATM, or from any person having used or serviced an ATM, where the offense is committed in connection with such use or service, or from any owner or operator of any network-connected ATM while such person is engaged in transporting or delivering property that is to be inserted into any such ATM, or from any person engaged in such transport or delivery under contract with, or employment by, any such owner or operator, or who extorts or attempts or conspires to obtain by extortion, any property or money or any other thing of value from any such person described in this subsection, shall be fined under this title or imprisoned not more than 20 years, or both. (b) Offenses against property (1) Offenses exceeding $1,000 Whoever breaks into, tampers with, damages, removes, steals, or attempts to break into, tamper with, damage, remove, or steal any ATM without authorization of the owner or operator of any such ATM, and removes or attempts to remove any property or money from any such ATM exceeding $1,000, shall be fined under this title or imprisoned not more than 10 years, or both. (2) Offenses not exceeding $1,000 Whoever breaks into, tampers with, damages, removes, steals, or attempts to break into, tamper with, damage, remove, or steal any ATM without authorization of the owner or operator of any such ATM, and does not remove or attempt to remove any property or money from any such ATM exceeding $1,000, shall be fined under this title or imprisoned not more than 1 year, or both. (c) Receipt, possession, concealment, storage, barter, sale, or disposal of property acquired unlawfully under this section Whoever receives, possesses, conceals, stores, barters, sells, or disposes of, any property or money or other thing of value that has been taken in violation of subsection (a) or (b), or conspires to do so, knowing the same to be property that has been unlawfully taken, shall be subject to the punishment provided in subsection (a) or (b), as applicable, for the taker. (d) Assault in connection with offenses Whoever, in committing, or in attempting to commit, any offense defined in subsection (a) or (b), forcibly assaults any person, or puts in jeopardy the life of any person by the use of a dangerous weapon or device, shall be fined under this title or imprisoned not more than 25 years, or both. (e) Killing or forcible accompaniment in connection with offenses Whoever, in committing any offense defined in this section, or in avoiding or attempting to avoid apprehension for the commission of such offense, or in freeing himself or attempting to free himself from arrest or confinement for such offense, kills any person, or forces any person to accompany the offender without the consent of such person, shall be imprisoned not less than 10 years, or, if death results, shall be punished by life imprisonment. (f) Definitions In this section: (1) ATM The term ATM \u2014 (A) means any network-connected automated teller machine terminal that is connected to 1 or more of the global, national, or regional electronic financial networks that allow a depositor of any bank, credit union, or savings and loan association, by use at such automated teller machine of a card or other access device, as defined in section 1029(e)(1), issued or authorized by such depository institution, to access the account of the depositor for the purpose of making withdrawals from or deposits to such account, or making inquiry as to the balance in such account; and (B) includes any automated teller machine owned, operated, or sponsored by a bank, credit union, or any savings and loan association, regardless of whether\u2014 (i) the automated teller machine is located on the physical premises of such an institution; or (ii) the automated teller machine is owned or operated by such an institution. (2) Bank; credit union; savings and loan association The terms bank , credit union , and savings and loan association have the meanings given those terms in section 2113. (3) Extortion The term extortion has the meaning given the term in section 1951(b)(2). (g) Included offenses The offenses defined in subsections (a) and (b) include any such offense committed against or involving an ATM, or any person using or servicing, or attempting to use or service, or against a person having used or serviced an ATM, where the offense is committed in connection with, or by reason of, such use or service, and any such offense against any owner or operator of an ATM while such person is engaged in transporting or delivering property that is to be loaded into an ATM, or against any person engaged in such transport or delivery under contract with, or employment by, any such owner or operator. .\n##### (b) Clerical amendment\nThe table of sections for chapter 103 of title 18, United States Code, is amended by inserting after the item relating to section 2113 the following:\n2113A. ATM robbery and incidental crimes. .\n#### 3. Offenses related to bank robbery and incidental crimes\nSection 2113(a) of title 18, United States Code, is amended\u2014\n**(1)**\nin the first paragraph, by striking force and violence and inserting force or violence ; and\n**(2)**\nby inserting or conspires to take, before from the person or presence of another, .",
      "versionDate": "2026-03-05",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-05-01T18:55:43Z"
          },
          {
            "name": "Crimes against property",
            "updateDate": "2026-05-01T18:55:33Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2026-05-01T18:55:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-27T15:10:04Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3798is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3798rs.xml"
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
      "title": "Safe Access to Cash Act of 2026",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-03-07T04:13:23Z"
    },
    {
      "title": "Safe Access to Cash Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safe Access to Cash Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T06:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to establish criminal offenses with respect to violations involving ATMs, regardless of whether the ATM is located on the physical premises of a financial institution, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T06:18:29Z"
    }
  ]
}
```
