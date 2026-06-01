# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6092?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6092
- Title: Constitutional Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 6092
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2025-12-05T22:03:56Z
- Update date including text: 2025-12-05T22:03:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6092",
    "number": "6092",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "J000288",
        "district": "4",
        "firstName": "Henry",
        "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
        "lastName": "Johnson",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Constitutional Accountability Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:03:56Z",
    "updateDateIncludingText": "2025-12-05T22:03:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:03:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6092ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6092\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Johnson of Georgia introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo ensure that the United States, States, and local governments are liable for monetary damages for constitutional violations by law enforcement officers.\n#### 1. Short title\nThis Act may be cited as the Constitutional Accountability Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe 14th Amendment to the Constitution of the United States was passed by Congress and ratified by the people of the United States against the backdrop of numerous State laws, policies, and practices that denied African Americans and others their enjoyment of fundamental rights.\n**(2)**\nCongress drafted the 14th Amendment to broadly protect fundamental rights and guarantee equality to all persons.\n**(3)**\nTo help realize the promise of equality protected in the 14th Amendment, Congress passed section 1979 of the Revised Statutes ( 42 U.S.C. 1983 ) (referred to in this section as section 1983 ), creating a statutory remedy for violations of the Constitution of the United States and Federal law. According to Mitchum v. Foster, 407 U.S. 225, 242 (1972), section 1983 was intended to interpose the Federal courts between the States and the people, as guardians of the people\u2019s Federal rights .\n**(4)**\nBy creating this remedy, Congress recognized that civil suits are a necessary and powerful tool to protect individual rights. Suits under section 1983 can not only make whole victims who are wronged. The suits can incentivize actors to take the steps necessary to avoid wrongdoing in the first place.\n**(5)**\nUnfortunately, the Supreme Court\u2019s current crabbed interpretation of section 1983 undermines its ability to accomplish these goals.\n**(6)**\nPrivate employers are responsible for the torts of their employees under the doctrine of respondeat superior. The risk of liability incentivizes private employers to effectively hire, supervise, train, and discipline their employees.\n**(7)**\nIn contrast, under Monell v. Department of Social Services of the City of New York, 436 U.S. 658 (1978), municipal defendants are not subject to respondeat superior liability for the constitutional torts of their officers. Cities may only be held liable for the constitutional torts of their officers only when the plaintiff can show that the violation was the result of a municipal policy or custom. Under Will V. Michigan Department of State Police, 491 U.S. 58 (1989), States cannot be held liable at all.\n**(8)**\nThe Monell doctrine requires judges to resolve difficult questions regarding which officials are policymakers, whether an official was acting in State or local capacity, and municipalities\u2019 training and hiring processes.\n**(9)**\nIn Board of County Commissioners v. Brown, 520 U.S. 397, 430 (1997), Justice Breyer criticized this highly complex body of interpretive law and called for a reexamination of the legal soundness of the Monell doctrine. Numerous scholars, as well as other jurists, have criticized the Monell doctrine as convoluted, inconsistent, arbitrary, and unintelligible.\n**(10)**\nThere is no statutory cause of action for constitutional violations by Federal officials. Victims can only bring their claims if courts infer a cause of action, which they are increasingly unlikely to do.\n**(11)**\nPolice officers are regularly called upon to make split-second, life-or-death decisions. The current liability regime, however, is not sufficient to ensure that police departments adequately hire, train, supervise, and discipline their officers so that they can respond to these situations in a constitutional manner.\n**(12)**\nThere are over 18,000 police departments in the United States and no uniform standard on how officers should be trained. Departments generally require significantly more training on how to deploy force than when it is appropriate to do so. As recently as 2017, 34 States did not mandate de-escalation training for all officers.\n**(13)**\nA National Public Radio study of fatal police shootings of unarmed Black people nationwide found that several officers were involved in multiple shootings without consequences. The same study found that departments hired officers with histories of domestic violence, as well as officers who were fired or forced out of other police departments due to prior misconduct.\n**(14)**\nAccording to United States v. Georgia, 546 U.S. 151, 158 (2006), Congress has the power under section 5 of the 14th Amendment to the Constitution of the United States to provide for direct enforcement of section 1 of the 14th Amendment by creating private remedies, including ones against the States. .\n**(15)**\nEliminating restrictions on the liability of State and local governments is necessary to ensure that no State [shall] deprive any person of life, liberty, or property, without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws. .\n#### 3. Civil actions for deprivation of rights\nSection 1979 of the Revised Statutes ( 42 U.S.C. 1983 ) is amended\u2014\n**(1)**\nin the first sentence, by striking Every and inserting the following:\n(a) In this section: (1) The term person includes\u2014 (A) the United States; (B) a State or Territory or the District of Columbia; (C) a local government; (D) an agency, government body, or any subdivision of the United States, a State or Territory or the District of Columbia, or a local government, or an entity created by a combination of any of the foregoing; and (E) an individual or private entity. (2) The term law enforcement officer includes any officer of a local government, or of a State or Territory or the District of Columbia, or of the United States, or an entity created by a combination of any of the foregoing who is empowered by law to execute searches, to seize evidence, or to make arrests for violations of law. (b) Every ;\n**(2)**\nin subsection (b), as so designated, in the first sentence, by inserting the United States, before any State ; and\n**(3)**\nby adding at the end the following:\n(c) A person is liable under this section for a violation of rights, privileges, or immunities secured by the Constitution and laws committed by an individual who at the time of the violation is employed by the person as, or contracted by the person to do the work of, a law enforcement officer. Liability under this subsection shall exist without regard to whether such employee or contractor would be immune from liability, and without regard to whether the employee or contractor was acting pursuant to a policy or custom of the person who is the employer. (d) Pursuant to section 5 of the 14th Amendment, no State shall be immune from suit, under the Eleventh Amendment or other doctrine of State sovereign immunity, for any claims on which subsection (c) subjects a person to liability. (e) For purposes of an action under subsection (c), the United States waives its sovereign immunity. (f) Except as expressly stated, no provision of this section shall be construed to abolish, repeal, or limit the scope of any right of action otherwise available under this section or any other source of law. .",
      "versionDate": "2025-11-18",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-11-18",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3186",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Constitutional Accountability Act",
      "type": "S"
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-12-02T15:25:04Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6092ih.xml"
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
      "title": "Constitutional Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Constitutional Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T01:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that the United States, States, and local governments are liable for monetary damages for constitutional violations by law enforcement officers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-27T01:48:21Z"
    }
  ]
}
```
